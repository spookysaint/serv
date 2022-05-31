from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io
from flask import Flask, render_template, request, jsonify, Response
from werkzeug.utils import secure_filename
import uuid, os, pathlib

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

def uploadFile(file_name):
    file_metadata = {
    'name': file_name,
    'mimeType': '*/*',
    "parents": ['1wnUgeiT-_sd_3mXqA37g4hrWnTX5R7ny']}
    media = MediaFileUpload(file_name,
                            mimetype='*/*',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id', supportsAllDrives=True).execute()
    print('File ID: ' + file.get('id'))
def file(filetype, f):
    if '.mp4' or '.mkv' in filetype:
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        resp = "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>"
        return resp

    elif '.png' or '.jpg' or '.jpeg' in filetype:
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        resp = "<img src='https://backend.rishabh.ml/0:/" + filename + "'>"
        return resp

    elif '.mp3' in filetype:
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        resp = "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/audio/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>"
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
    
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_fileto():
   if request.method == 'POST':
      f = request.files['file']
      if '.png' or '.jpg' or '.jpeg' or '.mp4' or '.mkv' or '.mp3' or '.pdf' in f.filename:
        
        if '.png' in f.filename:
            #res = file('.png', f)
            return Response(file('.png', f), mimetype='text/txt')
        if '.jpg' in f.filename:
            return Response(file('.jpg', f), mimetype='text/txt')
        
        if '.jpeg' in f.filename:
            return Response(file('.jpeg', f), mimetype='text/txt')
        
        if '.mkv' in f.filename:
            return Response(file('.mkv', f), mimetype='text/txt')
        
        if '.mp4' in f.filename:
            return Response(file('.mp4', f), mimetype='text/txt')

        if '.mp3' in f.filename:
            return Response(file('.mp3', f), mimetype='text/txt')
        
        if '.pdf' in f.filename:
            filename = f.filename
            f.save(filename)
            uploadFile(filename)
            os.remove(filename)
            resp = "https://backend.rishabh.ml/0:/" + filename
            return Response(resp, mimetype='text/txt')
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
