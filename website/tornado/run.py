import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.escape

from tornado.escape import json_decode, json_encode

import hashlib 
import json

import sys, os
sys.path.append('/home/spurs/tacotron/')
import argparse
import os
import re
import numpy as np
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer
from util import audio

os.environ['CUDA_VISIBLE_DEVICES'] = ''

parser = argparse.ArgumentParser()

parser.add_argument('--checkpoint', default='/home/spurs/tacotron/logs-tacotron/model.ckpt-274000', help='Path to model checkpoint')
#parser.add_argument('--reference_audio', default='/home/spurs/p264_071.wav', help='Reference audio path')
parser.add_argument('--mel_targets', default=None, help='Mel-targets path, used when use teacher_force generation')
#parser.add_argument('--text', required=True, default=None, help='Single test text sentence')

args = parser.parse_args()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



synth = Synthesizer(teacher_forcing_generating=False)
synth.load(args.checkpoint, reference_mel=True)

'''
ref_wav = audio.load_wav(args.reference_audio)
reference_mel = audio.melspectrogram(ref_wav).astype(np.float32).T
'''

iteration = args.checkpoint.split('-')[-1]
#speaker = args.reference_audio.split('/')[-1].split('_')[0]
base = '/home/spurs/website/tornado/static/res/'

mels = {"p225": "/home/spurs/website/tornado/static/wav/p225.npy", "p285": "/home/spurs/website/tornado/static/wav/p285.npy", 
            "p300": "/home/spurs/website/tornado/static/wav/p300.npy", "p360": "/home/spurs/website/tornado/static/wav/p360.npy"
            }

wavs = {"p225": "/home/spurs/website/tornado/static/wav/p225_024.wav", "p285": "/home/spurs/website/tornado/static/wav/p285_116.wav",
            "p300": "/home/spurs/website/tornado/static/wav/p300_148.wav", "p360": "/home/spurs/website/tornado/static/wav/p360_024.wav"
            }

for p in mels:
    wav = mels[p].replace('npy', 'wav')
    if not os.path.exists(wav):
        wav = audio.load_wav(wavs[p])
        mel = audio.melspectrogram(wav).astype(np.float32).T
        np.save(mels[p], mel, allow_pickle=False)   

class index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class generate_tts(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, *args):
        data = json_decode(self.request.body)
        #data = tornado.escape.json_decode(self.request.body)
        #data = json.decode(self.request.body)
        #txt = data.get('txt')
        speaker = data['speaker']
        reference_mel = np.load(mels[speaker])
        
        txt = data['txt'].lower()
        md5 = hashlib.md5(txt.encode('utf-8')).hexdigest()
        wav = os.path.join(base, 'iter_{0}_speaker_{1}_{2}.wav'.format(iteration, speaker, md5))
        img = os.path.join(base, 'iter_{0}_speaker_{1}_{2}.png'.format(iteration, speaker, md5))

        flag = 1

        if os.path.exists(wav):
            flag = 0

        if flag == 1:
            print('generating...')
            with open(wav, 'wb') as f:
                f.write(synth.synthesize(txt, mel_targets=None, reference_mel=reference_mel, alignment_path=img))

        ret = {}
        img = os.path.join('/static/res', 'iter_{0}_speaker_{1}_{2}.png'.format(iteration, speaker, md5))
        wav = os.path.join('/static/res', 'iter_{0}_speaker_{1}_{2}.wav'.format(iteration, speaker, md5))

        ret['img'] = img 
        ret['wav'] = wav 
        ret['txt'] = txt
        ret['speaker'] = speaker

        self.write(json_encode(ret))
        self.finish()


class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r'/', index),
            (r'/generate_tts', generate_tts),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    print('10.5.1.49:9000')
    server.listen(9000)
    tornado.ioloop.IOLoop.instance().start()
