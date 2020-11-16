# -*- coding: utf-8 -*-

import xmlrpclib

def connect(url,port,db,username,pwd):
    url = '%s:%s/xmlrpc/common'%(url,port)
    sock = xmlrpclib.ServerProxy(url)
    uid = sock.login(db,username,pwd)
    return uid

def get_data(url,port,db,uid,pwd):
    url = '%s:%s/xmlrpc/2/object'%(url,port)
    sock = xmlrpclib.ServerProxy(url)
    #item_ids = sock.execute(db,uid,pwd,'hr.social.item.type','search',[])
    #items = sock.execute(db,uid,pwd,'hr.social.item.type','read',item_ids,['name','short_name'])
    #print 'item type is %s' % items
    items_2 = sock.execute(db,uid,pwd,'hr.social.item.type','search_read',[],['name','short_name'])

    country_ids = sock.execute(db,uid,pwd,'res.country','search',[['code','=','CN']])
    provines = sock.execute(db,uid,pwd,'res.country.state','search_read',[['country_id','in',country_ids]],['id','name'])
    print 'provines is %s' % provines

    print 'items_2 is %s' % items_2
    #sock.execute_kw(db, uid, pwd,'res.partner','read',[1,3,2,5,6,4],['name'])

def get_data_from_odoo():
    db = 'banan'
    uid = 1
    pwd = 'p@ssw0rd'
    url = 'http://120.26.81.93:9000/xmlrpc/2/object'
    sock = xmlrpclib.ServerProxy(url)
    res = sock.execute_kw(db,uid,'p@ssw0rd','mail.message','search_read',[[['model','=','mail.group']]],{'fields':['model','subject','date','body'],'limit':1,'order':'id desc'})
    res = res[0]
    #print res['body']
    s = res['body']
    print type(s),s
    s = res['body'].encode('utf8')
    print type(s),s
    #import pdb
    #pdb.set_trace()
    e = res['body'].encode('utf8')
    #e = res['body']
    #import cgi
    #e = cgi.escape(e)
    #e = "中国"
    #e = "<b>HelloM</b> \n Hell o\n skkssks"
    news = [
        {'title':res['date'],'description':e,'url':"http://www.sina.com",'picurl':"http://www.sinaimg.cn/dy/slidenews/1_img/2015_17/2841_567113_575641.jpg"}
        #{'title':res['date'],'description':e,'url':"http://www.sina.com",'picurl':""}
    ]
    return news

def send_message():
    from  webchartapi import NewsMessage,WebChartApi
    sCorpID = "wx2b6a644956aea8d6"
    corpsecret = "LB437Fd5jpguFMfNV2wecwZ-5UBTlulbSLW78Qmt1hXnUD3RG8tTn0LIZO8mYwJz"
    api = WebChartApi(sCorpID,corpsecret)
    token = api.get_access_token()
    #news = [
    #    {'title':"This is a demo",'description':"description",'url':"http://www.sina.com",'picurl':"http://www.sinaimg.cn/dy/slidenews/1_img/2015_17/2841_567113_575641.jpg"}
    #]
    news = get_data_from_odoo()
    message = NewsMessage(3,touser="tedi3231",news=news)
    res = api.send_message(token,message)
    print 'res = %s, token is %s' %(res, token)


if __name__ == "__main__":
    #uid = connect('http://114.215.192.144','8069','policy','admin','admin')
    #print 'uid = %s' % uid
    #get_data('http://114.215.192.144','8069','policy',uid,'admin')
    send_message()
