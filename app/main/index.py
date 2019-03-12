from . import main
from flask import render_template

@main.route("/")
def dashboard():
    return render_template('dashboard.html')
