from flask import Flask, request, redirect, json
from werkzeug.utils import secure_filename
from MidiParser import parse
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['mid'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            midi_info = parse(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {'title': midi_info.get_filename(),
                    'length': midi_info.get_minute() + ':' + midi_info.get_seconds(),
                    'bpm': midi_info.get_bpm(),
                    'body': midi_info.get_html_table()
                    }
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            return response

@app.route('/')
def root():
    return app.send_static_file('index.html')


def start_server():
    app.run()


if __name__ == "__main__":
    start_server()
