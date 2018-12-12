from app import app
from flask import request, render_template
import json

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
	
