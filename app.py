from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io
from flask import Flask, render_template, request, jsonify, Response, send_file
from werkzeug.utils import secure_filename
import uuid, os, pathlib

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

def uploadFile(file_name, mime):
    file_metadata = {
    'name': file_name,
    'mimeType': mime,
    "parents": ['1wnUgeiT-_sd_3mXqA37g4hrWnTX5R7ny']}
    media = MediaFileUpload(file_name,
                            mimetype=mime,
                            resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id', supportsAllDrives=True).execute()
    print('File ID: ' + file.get('id'))

image = {'.jpg', '.jpeg', '.png'}
video = {'mp4', 'mkv'}
audio = {'mp3', 'ogg'}
def file(filetype, f):
    filename = str(uuid.uuid4()) + filetype
    with open('logs.txt', 'a+') as fa:
        fa.write(request.headers.get('X-Forwarded-For', request.remote_addr) + ' uploaded ' + filename)
    if filetype in video:
        f.save(filename)
        uploadFile(filename, 'video/mp4')
        os.remove(filename)
        resp = "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "&load=none' height='360' width=100% allowfullscreen=True></iframe></div>"
        return resp

    elif filetype in image:
        f.save(filename)
        uploadFile(filename, 'image/jpg')
        os.remove(filename)
        resp = "<img src='https://backend.rishabh.ml/0:/" + filename + "'>"
        return resp

    elif filetype in audio:
        f.save(filename)
        uploadFile(filename, 'audio/mpeg')
        os.remove(filename)
        resp = "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/audio/?url=https://backend.rishabh.ml/0:/" + filename + "&load=none' height='360' width=100% allowfullscreen=True></iframe></div>"
        return resp

      #import werkzeug
app = Flask(__name__)

# def filesend(filetype):
#     filename = str(uuid.uuid4()) + filetype
#     f.save(filename)
folder = 'uploaded_files'
@app.route('/')
def upload_file():
   return render_template('index.html')
    
@app.route('/loggs')
def log():
   return send_file('logs.txt', mimetype='text/plain')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_fileto():
   if request.method == 'POST':
      f = request.files['file']
      if '.png' or '.jpg' or '.jpeg' or '.mp4' or '.mkv' or '.mp3' or '.pdf' in f.filename:
        if '.png' in f.filename:
            res = file('.png', f)
            return render_template('response.html', embedcode=res)
        if '.jpg' in f.filename:
            res = file('.jpg', f)
            return render_template('response.html', embedcode=res)        
        if '.jpeg' in f.filename:
            res = file('.jpeg', f)
            return render_template('response.html', embedcode=res)
        
        if '.mkv' in f.filename:
            res = file('.mkv', f)
            return render_template('response.html', embedcode=res)
        
        if '.mp4' in f.filename:
            res = file('.mp4', f)
            return render_template('response.html', embedcode=res)

        if '.mp3' in f.filename:
            res = file('.mp3', f)
            return render_template('response.html', embedcode=res)
        
        if '.pdf' in f.filename:
            filename = f.filename
            f.save(filename)
            uploadFile(filename)
            os.remove(filename)
            resp = "https://backend.rishabh.ml/0:/" + filename
            return render_template('response.html', embedcode=res)
        # filename = str(uuid.uuid4()) + filetype
        # f.save(filename)
        # uploadFile(filename)
        # os.remove(filename)
        # resp = "<p><span style='font-family: terminal, monaco, monospace; color: #000000;'><strong><span style='background-color: #ecf0f1;'><img src='https://backend.rishabh.ml/0:/" + filename + "'></span></strong></span></p>"
        # resp.mimetype = 'text/plain'
        # return resp
      # if '.mp4' or '.mkv' in f.filename:
        # filetype = '.mp4'
        # filename = str(uuid.uuid4()) + filetype
        # f.save(filename)
        # uploadFile(filename)
        # os.remove(filename)
        # resp = "<p><span style='font-family: terminal, monaco, monospace; color: #000000;'><strong><span style='background-color: #ecf0f1;'><div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div></span></strong></span></p>"
        # resp.mimetype = 'text/plain'
        # return resp
      else:
        return "Your Uploaded File Type is Not Avilable for Upload Ask @Rishabhmoodi For the same"
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
