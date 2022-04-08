from flask import Flask, render_template, request, redirect, url_for, flash
import json
from imgur_stuff import Imgur

with open('secrets.json') as json_file:
    secrets = json.load(json_file)
app = Flask(__name__)
app.templates_auto_reload = True
app.secret_key = secrets['secret_key']
imgur = Imgur(secrets['imgur_client_id'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['picture']
        allowed_extensions = ['jpg', 'png']
        if file.filename.split('.')[1] in allowed_extensions:
            link = imgur.uploadImage(
                file, f"Djs2022_{request.form['name']}_THE", "THIS FILE IS BEING USED TO SERVE THE PAGE AT https://djs2022.tk")
            if not link:
                flash(f'File Upload failed. Please try again in some time.')
                return redirect(url_for('index'))
            public_data = {
                "Name": request.form['name'],
                "instagram": request.form['instagram'],
                "tagline": request.form['tagline'],
                "img_link": link
            }
            private_data = {
                "Name": request.form['name'],
                "email": request.form['email'],
                "whatsapp_number": request.form['phone_number'],
                "instagram": request.form['instagram'],
                "tagline": request.form['tagline'],
                "img_link": link
            }
            if request.form['batch'] == "JEE":
                with open('./studentdata/jee.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(public_data)
                    new = json.dumps(old, indent=4)
                with open('./studentdata/jee.json', 'w') as f:
                    f.write(new)
                with open('./studentsprivate/jee.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(private_data)
                    new = json.dumps(old, indent=4)
                with open('./studentsprivate/jee.json', 'w') as f:
                    f.write(new)
            elif request.form['batch'] == "NEET":
                with open('./studentdata/neet.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(public_data)
                    new = json.dumps(old, indent=4)
                with open('./studentdata/neet.json', 'w') as f:
                    f.write(new)
                with open('./studentsprivate/neet.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(private_data)
                    new = json.dumps(old, indent=4)
                with open('./studentsprivate/neet.json', 'w') as f:
                    f.write(new)
            elif request.form['batch'] == "CET":
                with open('./studentdata/cet.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(public_data)
                    new = json.dumps(old, indent=4)
                with open('./studentdata/cet.json', 'w') as f:
                    f.write(new)
                with open('./studentsprivate/cet.json', 'r') as f:
                    old = json.load(f)
                    old['students'].append(private_data)
                    new = json.dumps(old, indent=4)
                with open('./studentsprivate/cet.json', 'w') as f:
                    f.write(new)
            else:
                flash("An error occured trying to resolve your batch. Please try again.")
                return redirect(url_for('index'))
            flash(f"Your image has been uploaded find it at: {link}")
            return redirect(url_for('success'))
        else:
            flash(f'Incorrect file type.')
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
