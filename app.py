from flask import Flask, render_template, request, redirect, url_for, flash
import json

with open('secrets.json') as json_file:
    secrets = json.load(json_file)
app = Flask(__name__)
app.templates_auto_reload = True
app.secret_key = secrets['secret_key']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['picture']
        flash(f'File {file.filename} uploaded successfully')
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
