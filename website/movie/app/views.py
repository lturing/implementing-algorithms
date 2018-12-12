from app import app
from flask import request, render_template
import json
from flask import send_from_directory
import os
from flask import make_response
import librosa 
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
import numpy as np 
import librosa.effects 
import os 
from io import BytesIO
import base64


def get_spectrograms(fpath):
    '''Returns normalized log(melspectrogram) and log(magnitude) from `sound_file`.
    Args:
      sound_file: A string. The full path of a sound file.
    Returns:
      mel: A 2d array of shape (T, n_mels) <- Transposed
      mag: A 2d array of shape (T, 1+n_fft/2) <- Transposed
    '''

    # Loading sound file
    sr = 16000 # sample rate 
    y, sr = librosa.load(fpath, sr=sr) # Audio will be automatically resampled to the given rate

    # Trimming
    #y, _ = librosa.effects.trim(y)

    # Preemphasis
    preemphasis = 0.97
    y = np.append(y[0], y[1:] - preemphasis * y[:-1])

    # stft
    n_fft = 1024
    hop_length = 200 #int(sr*0.0125)
    win_length = 800 #int(sr*0.05)

    linear = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length, win_length=win_length)

    # magnitude spectrogram
    mag = np.abs(linear)  # (1+n_fft//2, T)

    # mel spectrogram
    n_mels = 160
    mel_basis = librosa.filters.mel(sr, n_fft, n_mels)  # (n_mels, 1+n_fft//2)
    mel = np.dot(mel_basis, mag)  # (n_mels, t)

    # to decibel
    mel = 20 * np.log10(np.maximum(1e-5, mel))
    #mag = 20 * np.log10(np.maximum(1e-5, mag))

    # normalize
    ref_db = 20
    max_db = 100
    mel = np.clip((mel - ref_db + max_db) / max_db, 1e-8, 1)
    #mag = np.clip((mag - ref_db + max_db) / max_db, 1e-8, 1)

    # Transpose
    #mel = mel.T.astype(np.float32)  # (T, n_mels)
    #mag = mag.T.astype(np.float32)  # (T, 1+n_fft//2)
    return mel
    #return mel, mag


def plot_im(fpaths):
    titles = {'en':['en_mel-gram', 'en_spectrogram'], 'ch':['ch_mel-gram', 'ch_spectrogram']}
    keys = ['en', 'ch']
    ret = {}
    for i, k in enumerate(keys):
        fig = plt.figure()
        mel = get_spectrograms(fpaths[k])
        
        im = plt.imshow(mel, aspect='auto')
        #fig.subplots_adjust(left=0.07, bottom=0.05, right=0.9, top=0.92, wspace=0.18, hspace=0.30)
        cbar_ax = fig.add_axes([0.92, 0.05, 0.025, 0.87])
        fig.colorbar(im, cax=cbar_ax)
        #plt.title(titles[k][0], loc='center')
        
        save_file = BytesIO()
        plt.savefig(save_file, format='png')
        file_base64 = base64.b64encode(save_file.getvalue()).decode('utf-8')
        ret[k+'_mel'] = file_base64
        plt.close()
    
    return ret    
    

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html') 

@app.route('/generate_tts', methods = ['POST'])
def generate_tts():
	txt = request.form.get('txt');
	img = "http://222.20.72.51:88/media/uploads/Spurs/dog.jpg"
	wav = "http://222.20.72.51:88/media/uploads/Spurs/test.wav"
	ret = {}
	ret['txt'] = txt
	ret['wav'] = wav
	ret['img'] = img
	return json.dumps(ret)
	
@app.route('/movies/<path:filename>')
def custom_static(filename):
    return send_from_directory('/media/disk2/spurs/movie/movies', filename)

@app.route('/find', methods = ['POST'])
def find():
    idx = request.form.get('idx')
    paths = {
            0 : '/movies/The.Angry.Birds.Movie.2016.BluRay.720p.x264.AC3.4Audios/clips',
            1 : '/movies/Kung.Fu.Panda.2008.BluRay.720p.x264.AC3.4Audios/clips',
            2 : '/movies/Inside.Out.2015.BluRay.720p.x264.AC3.4Audios/clips',
            3 : '/movies/Madagascar.2014.BluRay.720p.x264.AC3.4Audios/clips',
            4 : '/movies/The.Jungle.Book.2016.BluRay.720p.x264.AC3.2Audios/clips',
            5 : '/movies/Big.Hero.6.2014.BluRay.720p.x264.AC3.4Audios/clips',
            6 : '/movies/Smurfs.2013.BluRay.720p.x264.AC3.4Audios/clips',
            7 : '/movies/Smurfs.The.Lost.Village.2017.BluRay.720p.x264.AC3.2Audios/clips'}

    k = int(idx.split('_')[0])
    with open('/home/spurs/website/movie/app/subtitles', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('|')
            idd = line[0]
            if idd == idx:
                en = line[-2]
                ch = line[-1]
                break
    try:
        root = '/media/disk2/spurs/movie'
        base = os.path.join(root, paths[k][1:])
        en_path = os.path.join(base, idx + '_en.wav')
        ch_path = os.path.join(base, idx + '_ch.wav')
        fpaths = {'en' : en_path, 'ch' : ch_path}

        ret = plot_im(fpaths)
        ret['en'] = os.path.join(paths[k], idx + '_en.wav')
        ret['ch'] = os.path.join(paths[k], idx + '_ch.wav')
        ret['en_txt'] = en
        ret['ch_txt'] = ch
    except KeyError:
        return make_response("", 501)

    return json.dumps(ret)
