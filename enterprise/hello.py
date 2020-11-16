# -*- coding: utf-8 -*-

import  tornado
import tornado.ioloop
from tornado.options import define, options
import tornado.web
from WXBizMsgCrypt import WXBizMsgCrypt
import urllib
import xml.etree.cElementTree as ET
import datetime
import requests
import xmlrpclib
#import  psycopg2


SToken = "tediloveniuniu"
appSecret = "d4624c36b6795d1d99dcf0547af5443d"
sCorpID = "wx32431e1f20e1f035"
sEncodingAESKey = "qRmvrrBE7IE9rB1g1uJkTpOPnErttEmSPrZ9yBs2HCG"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	print self.request.arguments
        msg_signature ,timestamp,echostr,nonce= self.get_arguments('signature'),self.get_argument('timestamp'),self.get_argument('echostr'),self.get_argument('nonce')
        print "msg_signature=%s,timestamp=%s,echostr=%s,nonce=%s"%(msg_signature,timestamp,echostr,nonce)
        echostr = urllib.unquote(echostr)
        print "msg_signature=%s,timestamp=%s,echostr=%s,nonce=%s"%(msg_signature,timestamp,echostr,nonce)
        wxcpt = WXBizMsgCrypt(SToken,sEncodingAESKey,sCorpID)
        ret,sEchoStr = wxcpt.VerifyURL(msg_signature[0],timestamp,nonce,echostr)
        print 'ret=%s,sEchoStr is %s'%(ret,sEchoStr)
        self.write(echostr)
    
    def post(self):
        print "hello "


application = tornado.web.Application([
    (r"/",MainHandler),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
