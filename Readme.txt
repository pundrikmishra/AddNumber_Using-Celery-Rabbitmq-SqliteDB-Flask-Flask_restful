 Install all this:-
     pip install flask
     pip install flask_restful
     pip install celery
     pip install sqlalchemy   #for backend database



 If using rabbitmq as a broker then first install it:-         #### if using celery then you need broker
        pip install rabbitmq       #if using pycharm then inside pycharm open Terminal and write this command
        sudo service rabbitmq-server start # from terminal
        sudo service rabbitmq-server status #from terminal check status
        sudo service rabbitmq-server stop
        if face any problem in installing then install it manually:- https://www.rabbitmq.com/download.html


For running program:-
                python main.py

For starting worker:-
                celery -A main.celery worker --loglevel=info

                ### celery -A yourfilename.celery worker --loglevel=info
                ### yourfilename = name of that file in which your celery app is running


url:-
     broker='amqp://guest:@localhost:5672//'   ### for rabbitmq
     backend='db+sqlite:///db.sqlite3'         ### Sqlite database as backend
     backend='rpc://'                          ### rabbitmq as backend
     backend='amqp'



1) TypeError: sequence item 0: expected str instance, Flask found

2)TypeError: Object of type AsyncResult is not JSON serializable
                :- For this make sure you call celery function do not return it
                :- for example in this project
                                        :- I called function like
                                                                     add.delay(2, 3)       #### do this
                                        :- and do not return function
                                                                     return add.delay(2, 3) ##### do not do this

3)if you start celery worker using command:-    celery -A yourfilename.celery worker --loglevel=info
              and face this error:-
                            Error:
                            Unable to load celery application.
                            'flask' object has no attribute 'user_options'

              :- Then check your file name, backend url, yourfilename = name of that file in which your celery app is running,

For more:-
    https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf
    https://flask.palletsprojects.com/en/1.0.x/patterns/celery/
    https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/07/03/Asynchronous%20Tasks%20in%20Python%20-%20Getting%20Started%20With%20Celery/celery_example
    https://www.cnblogs.com/fangwenyu/p/3625830.html
    https://www.cnblogs.com/fangwenyu/p/3625830.html
    https://www.youtube.com/watch?v=iwxzilyxTbQ
    https://www.youtube.com/watch?v=THxCy-6EnQM
    https://www.youtube.com/watch?v=etfECjhaP-g&list=PLXmMXHVSvS-CoYS177-UvMAQYRfL3fBtX&index=33
    https://www.youtube.com/watch?v=jsoC01eMHQA


##########################################################################################################################
##########################################################################################################################
#               THIS MEANS,THE NAME WE ASSIGN TO CELERY,
#               THAT SAME NAME IS USED TO START CELERY WORKER
#               LIKE:-
#                       celery -A YourFileName.SameName worker --loglevel=info
#
#               YourFileName = name of that file in which your celery app is running
#               SameName  =  THE NAME WE ASSIGN TO CELERY
#
# For example in main.py file:-
#      1)       app = Celery('main', broker='amqp://guest:@localhost:5672//', backend='db+sqlite:///db.sqlite3')
#                       Then to start celery worker:-
#                               celery -A main.app worker --loglevel=info
#                                       OR
#                               celery -A main worker --loglevel=info
#      2)        celery = Celery('main', broker='amqp://guest:@localhost:5672//', backend='db+sqlite:///db.sqlite3')
#                       Then to start celery worker:-
#                               celery -A main.celery worker --loglevel=info
#                                       AND NOT use below command
#                               celery -A main worker --loglevel=info      ### do not use this command due to some reason
##########################################################################################################################
##########################################################################################################################