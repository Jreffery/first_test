'''
Created on 2016/10/6

@author: Jeffery
'''

from twisted.internet import reactor
from cc.appweb.dims.factory import DimsFactory
if __name__ == '__main__':
    reactor.listenTCP(8000, DimsFactory())
    reactor.run()