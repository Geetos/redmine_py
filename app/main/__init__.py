from flask import Blueprint

main = Blueprint("main",__name__)

from . import welcome, account_auth, project