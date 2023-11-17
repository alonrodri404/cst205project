# impliment filters here

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask import url_for

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def index():
    def filters():
        p1 = '<p>waiting for filters</p>'
    return render_template("index.html", image_url=url_for('static', filename='images/tree.jpg'))

if __name__ == '__main__':
    app.run(debug=True)