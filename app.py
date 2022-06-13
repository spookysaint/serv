import io,uuid, base64, os, pathlib, requests
from flask import Flask, render_template, request, jsonify, Response, send_file

@app.route('/')
def upload_file():
   return render_template('index.html')
    
@app.route('/loggs')
def log():
   return send_file('logs.txt', mimetype='text/plain')

@app.route('/reload')
def reload():
   r = requests.get("https://gitlab.com/rishabh-modi2/public/-/raw/main/upload.py")
   open('app.py', 'wb').write(r.content)
   return "reloaded"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
