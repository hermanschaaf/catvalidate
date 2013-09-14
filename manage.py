#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os
import bottle
from datetime import date

from decanter.decanter import parse_args, Decanter
from decanter.lib.middleware import Dispatcher, StripPath
from decanter.lib.config import Config
from decanter.lib.logger import Log

if __name__ == '__main__':
    args = parse_args(filepath=__file__)

    config = Config(args.config)
    app = Dispatcher(StripPath(bottle.default_app()), config)
    pidfile = config.pidfile.format(args.port)

    # make directory to put pid file
    piddir = os.path.dirname(pidfile)
    if not os.path.isdir(piddir):
        os.makedirs(piddir)

    logfile = config.logger['filepath'].format(args.port, date.today())
    # initialize logger
    log = Log(logfile)
    decanter = Decanter(app, args.hostname, args.port, pidfile)

    # execute command
    {
        'start': lambda: decanter.start(),
        'stop': lambda: decanter.stop(),
        'status': lambda: decanter.status(),
        'restart': lambda: decanter.restart(),
        'runserver': lambda: decanter.runserver(),
    }[args.command]()
