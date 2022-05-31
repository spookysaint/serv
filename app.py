from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import uuid, os

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

def uploadFile(filename)
        os.remove(filename):
    file_metadata = {
    'name': filename,
    'mimeType': '*/*',
    "parents": ['1wnUgeiT-_sd_3mXqA37g4hrWnTX5R7ny']}
    media = MediaFileUpload(filename,
                            mimetype='*/*',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id', supportsAllDrives=True).execute()
    print ('File ID: ' + file.get('id'))
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
      if '.png' in f.filename:
        filetype = '.png'
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        return "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>"
      if '.mp4' in f.filename:
        filetype = '.mp4'
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        return jsonify("<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>")
      if '.jpg' in f.filename:
        filetype = '.jpg'
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        return "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>"
      if '.mkv' in f.filename:
        filetype = '.mp4'
        filename = str(uuid.uuid4()) + filetype
        f.save(filename)
        uploadFile(filename)
        os.remove(filename)
        return "<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/0:/" + filename + "' height='360' width=100% allowfullscreen=True></iframe></div>"
      else:
        return "Your Uploaded File Type is Not Avilable for Upload Ask @Rishabhmoodi For the same"
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
