# -*- coding: utf-8 -*-
from WXBizMsgCrypt import  WXBizMsgCrypt

sCorpID = "wx1bb2c78b19140a77"
import xmlrpclib
HOST = "http://114.215.192.141"
PORT = 8000
DB = "policy"
USER = "admin"
PASS = "admin123"

def getPolicies():
    url = '%s:%d' % (HOST,PORT)
    common_url = "%s/xmlrpc/2/common"%url
    common = xmlrpclib.ServerProxy(common_url)
    uid = common.authenticate(DB, USER, PASS, {})
    #print "Logged in as %s (uid:%d)" % (USER,uid)

    model_url = '{}/xmlrpc/2/object'.format(url)
    #print model_url
    models = xmlrpclib.ServerProxy(model_url)
    #print models.execute_kw(DB, uid, PASS,
    #'res.partner', 'check_access_rights',
    #['read'], {'raise_exception': False})
    #print models.execute_kw(DB,uid,PASS,'hr.employee','check_access_rights',['search'])
    emp_ids = models.execute_kw(DB,uid,PASS,'hr.employee','search',[[]])
    category_ids = models.execute_kw(DB,uid,PASS,'hr.reward.policy.category','search',[[]])
    #print category_ids
    employess = models.execute_kw(DB,uid,PASS,'hr.employee','read',[emp_ids],{'fields':['name']})
    mypolicy_ids = models.execute_kw(DB,uid,PASS,'hr.employee','get_policies_from_category',[],{"category_ids":1,"ids":[1,2]})




def testEnc():
    data = """"<xml><ToUserName><![CDATA[wx1bb2c78b19140a77]]></ToUserName><FromUserName><![CDATA[85920312]]></FromUserName><CreateTime>1421738549</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[南京天气预报【实况】温度11℃ 湿度44%% 东风3级 发布时间：14:55【较冷】建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。01月20日 周二 多云转阴 12℃~4℃ 东南风 3-4级 日出日落：07:05~17:2701月21日 周三 多云 11℃~-1℃ 西北风 4-5级 日出日落：07:05~17:2801月22日 周四 晴 8℃~-3℃ 西北风 3-4级 日出日落：07:04~17:29]]></Content><MsgId>1234567890123456</MsgId><AgentID>128</AgentID></xml>"""
    token = "VFPr2vH2OioFRkjaxM"
    aeskey = "2dqnNYe8Z7gXY1Nf1dcaoLdfULFKcq4AzHekVuorq5F"
    timestamp="1421738549"
    nonce="202298095"
    wxcpt = WXBizMsgCrypt(token,aeskey,sCorpID)
    ret,sEncryptMsg=wxcpt.EncryptMsg(data, nonce, timestamp)
    print "ret=%s,sEncryptMsg=%s" % (ret,sEncryptMsg)

if __name__ == "__main__":
    getPolicies()
