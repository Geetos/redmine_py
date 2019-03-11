# coding:utf-8
from app import create_app

app = create_app('dev')

if __name__=='__main__':
    app.run(threaded = True, debug = True)