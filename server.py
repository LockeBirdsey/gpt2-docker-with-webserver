import os
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from gpt2_process import GPT2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
NO_FILE = "NOFILE"
app.config['CORPUS_FILE_NAME'] = NO_FILE


@app.route('/')
def index(file_name=NO_FILE, results=None):
    if file_name != NO_FILE:
        app.config['CORPUS_FILE_NAME'] = file_name
    return render_template("index.html", file_name=app.config['CORPUS_FILE_NAME'], results=results)


@app.route('/upload')
def upload_file_start():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f_name = secure_filename(f.filename)
        f.save(f_name)
        file_name = str(f_name)
        print(file_name)
        return index(file_name=file_name)
        # return 'file uploaded successfully and stored at {}'.format(f.filename)


@app.route('/run_process')
def start_process():
    f_name = app.config['CORPUS_FILE_NAME']
    if f_name == NO_FILE:
        return index()
    file_name = f_name  # since the Flask UPLOAD_FOLDER doesn't do anything
    out = []
    with open(file_name, 'r', encoding='utf-8') as f:
        out = f.read()
    print(out)
    gpt2 = GPT2()
    model_name = os.environ['GPT2_MODEL_NAME']
    sess = gpt2.finetune(file_name=file_name, model_name=model_name)
    gen = []
    for i in range(20):
        gen.append(gpt2.generate_text(sess))
    print(gen)
    return ""


if __name__ == '__main__':
    app.run(debug=True)
