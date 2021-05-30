from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

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
        # TODO This is where we call gpt2
        # process(f.filename, )
        print(f)
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
