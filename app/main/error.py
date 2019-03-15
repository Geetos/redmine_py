from flask import render_template
from . import main
from .. import logger

@main.route('/error')
@main.errorhandler(400)
@main.errorhandler(404)
def error(e):
    logger.info("error occurred : %s" % e)
    try:
        code = e.code
        if code == 404:
            return render_template("error.html",error_info = code)
    except Exception as e:
        logger.info("exception is %s" % e)
    finally:
        return render_template("error.html", error_info = 'Unknown Error')
    
