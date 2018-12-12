from flask import Flask
#from flask import send_from_directory

app = Flask(__name__)

from app import views
'''
@app.route('/movies/<path:filename>')
def custom_static(filename):
    return send_from_directory('/media/disk2/spurs/movie/movies', filename)
'''

