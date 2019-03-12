from flask import Blueprint

main = Blueprint("main",__name__)

from . import index, homepage, account_auth, project