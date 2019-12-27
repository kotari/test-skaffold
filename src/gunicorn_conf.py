import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
# bind = '127.0.0.1:8080'
bind = '0.0.0.0:5000'
proc_name = 'gunicorn_test'
pidfile = '/tmp/gunicorn_test.pid'
logfile = '/tmp/gunicorn_test.log'
worker_class = 'sync'
timeout = 3600
debug = False
max_requests = 0
preload_app = True
# reload = True
