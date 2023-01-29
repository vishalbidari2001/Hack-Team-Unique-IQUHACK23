from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        result = subprocess.run(["python", file.filename], stdout=subprocess.PIPE)
        return result.stdout
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(port=8000)
