from environment import *
import os

home = lambda filename: os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), filename)

# default routes
default = {
    'bundle': 'cats',
    'controller': 'index'
}

# logging
logger = {
    # log directory path, first {0} is the port number and second {1] is the date
    'filepath': log_path if os.path.isabs(log_path) else home(log_path),
    # DEBUG, INFO, WARNING, ERROR, FATAL
    'level': 'DEBUG'
}

# pid file
pidfile = pidfile_path if os.path.isabs(
    pidfile_path) else home(pidfile_path)

# list of plugins names to install by default
plugins = ['jinja2']

apppath = home('app')

assets_path = 'assets'