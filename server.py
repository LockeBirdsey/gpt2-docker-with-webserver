import os
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from gpt2_process import GPT2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/upload')
def upload_file_start():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f_name = secure_filename(f.filename)
        f.save(f_name)
        # This is where we call gpt2
        gpt2 = GPT2()
        model_name = os.environ['GPT2_MODEL_NAME']
        file_name = Path(app.config['UPLOAD_FOLDER']).joinpath(f_name)
        sess = gpt2.finetune(file_name=file_name, model_name=model_name)
        gen = []
        for i in range(20):
            gen.append(gpt2.generate_text(sess))
        print(gen)
        return '\n'.join(gen)
        # return 'file uploaded successfully and stored at {}'.format(f.filename)


if __name__ == '__main__':
    app.run(debug=True)
