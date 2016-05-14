#!/usr/bin/env python3
import bottle
import gevent.monkey

import service.example


@bottle.route('/static/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='./static')


@bottle.get('/')
def index():
    return {'Hello': service.example.C.greet('Marco')}


if __name__ == '__main__':
    gevent.monkey.patch_all()

    bottle.debug(True)
    bottle.run(**{
        'host': '0.0.0.0',
        'port': 8000,
        'server': 'gevent'
    })
