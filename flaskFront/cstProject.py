from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template("index.html", image_url=url_for('static', filename='images/tree.jpg'))

@app.route('/filters', methods=['POST'])
def filters():
    if request.form['filter'] == 'Generate Pictures':
        # Implement your logic to generate pictures
        pass
    elif request.form['filter'] == 'Apply Filter':
        # Redirect to the filter selection page
        return redirect(url_for('filter_selection'))

    return redirect(url_for('index'))

@app.route('/filter_selection')
def filter_selection():
    return render_template("filter_selection.html", image_url=url_for('static', filename='images/tree.jpg'))

if __name__ == '__main__':
    app.run(debug=True)
