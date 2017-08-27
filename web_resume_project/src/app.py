__author__ = 'SGarcia'

from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.secret_key = 'sebbybear'

@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/extracurriculars')
def extracurriculars_template():
    return render_template('extracurriculars.html')

@app.route('/projects')
def projects_template():
    return render_template('projects.html')

@app.route('/certificates')
def cerificates_template():
    return render_template('certificates.html')

@app.route('/resources')
def resources_template():
    return render_template('resources.html')

@app.route('/adtech-project')
def adtech_template():
    return render_template('adtech_project.html')

@app.route('/logistic-regression-project')
def logreg_template():
    return render_template('logreg_project.html')

@app.route('/scraper-project')
def scraper_template():
    return render_template('scraper_project.html')

if __name__ == '__main__':
    app.run(debug=True)