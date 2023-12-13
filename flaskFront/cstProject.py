# Alondra Rodriguez: Hello, I worked on the backend functions of the code. I made sure that every button was working when pressed and made the filters/filter sliders. 
# I worked with Daniel Solano, another backend programmer, and we helped each other with the animal random picture generator to display in main, including creating an upload button that is functional. 

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from backend import generate_animal_pictures
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'  # Set your upload folder
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'animal_1.jpg')
            file.save(save_path)
            return redirect(url_for('index'))

    return render_template("upload.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'animal_1.jpg')
            file.save(save_path)
            return redirect(url_for('index'))

    image_url = url_for('static', filename='images/animal_1.jpg') if os.path.exists('static/images/animal_1.jpg') else None
    return render_template("index.html", image_url=image_url)

@app.route('/filters', methods=['POST'])
def filters():
    if request.form['filter'] == 'Generate Pictures':
        image_urls = generate_animal_pictures()  # This will return a list of image URLs
        return render_template("index.html", image_urls=image_urls)
    elif request.form['filter'] == 'Apply Filter':
        # Redirect to the filter selection page
        return redirect(url_for('filter_selection'))

    return redirect(url_for('index'))

@app.route('/gallery')
def gallery():
    return render_template("index1.html")


@app.route('/filter_selection')
def filter_selection():
    return render_template("filter_selection.html", image_url=url_for('static', filename='images/animal_1.jpg'))

if __name__ == '__main__':
    app.run(debug=True)
