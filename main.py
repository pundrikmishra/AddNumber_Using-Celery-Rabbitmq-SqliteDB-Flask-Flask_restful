from flask import Flask
from flask_restful import Resource, Api
from celery import Celery

app = Flask(__name__)
api = Api(app)

celery = Celery('main', backend='rpc://', broker='amqp://guest:@localhost:5672//')
@celery.task
def add(x, y):
    return x + y
# def hello():
#     # print("celery is working")  # this is not working
#     return 'hello amit'      # only this work

class HelloWorld(Resource):
    def get(self):
        add.delay(2, 3)          # 1) first function
        # hello.delay()           # 2) second function
        # r = hello.delay()       # 3) third function  for this function to execute first start celery worker, otherwise flask_app url loding and loding.......
        # return r.get()          # 3) third function
        return "Hello World"
        # return add.delay(2, 3)  # 4) Fourth Function ## do not do this, otherwise you face error like:- TypeError: Object of type AsyncResult is not JSON serializable
        # return hello()          # 5) Fifth Function  ## do not do this, otherwise you face error like:- TypeError: Object of type AsyncResult is not JSON serializable



api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
