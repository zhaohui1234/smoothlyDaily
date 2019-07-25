from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import loader
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from lxml import etree
import time
from django.utils.encoding import smart_str


activity_name = "全域科普"

def autoResponse(request):
    #if request.

    if request.method == 'GET':
        return verify(request)
    else :
        return response(request)
    

def verify(request):
    
    print('verify for the wx')
    print(request)
        
    #print('\n'.join(('%s:%s' % item for item in request.__dict__.items())))
    print(request.POST.__dict__)
    print(request.body)
   
    data = request.GET    
 
    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get('nonce')
    echostr = data.get('echostr')

    print(signature, timestamp, nonce, echostr)

    token = "kpzx1kpzx2"

    list1 = [token, timestamp, nonce]
    list1.sort() 
    str_list = ''.join(list1)
    print (str_list)
    sha1 = hashlib.sha1()
    print(sha1)
    sha1.update(str_list.encode('utf-8'))
    hashcode = sha1.hexdigest()

    print("handle/GET func : hashcode, signature: " , hashcode, signature)
        
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("") 

# for auto response 
# for verify TOO !!!

def response(request):
    #if request.method == 'GET':

    #VAR.__seq__ = 0
    #user_dict={}  

 
    print('auto response')
    data = request.POST

    print('data is  %s ' % data )
   
    data = smart_str(request.body)
    print('data is  %s ' % data )
    
    str_xml = etree.fromstring(data)
    msgType = str_xml.find('MsgType').text
    
    print ("msgType is %s" % msgType)
    
    if msgType == "text":
        
        fromUser = str_xml.find('ToUserName').text
        toUser = str_xml.find('FromUserName').text
        content = str_xml.find('Content').text
        nowtime = str(int(time.time()))
        print("msgType is %s " % msgType)
        
        if content != activity_name:
            reply_content = '欢迎参加全域科普活动，请您回复“全域科普”，获取活动编码'
        else:
            if toUser in VAR.user_dict:
                number = VAR.user_dict[toUser]
                print ("The user firs request for number %d "% number) 
                reply_content = ("您已经领取活动编码，您的活动编码为 %03d " % number)
            else:
                VAR.__seq__ = VAR.__seq__+1
                VAR.user_dict[toUser] = VAR.__seq__       
                print("seq is %d " % VAR.__seq__)
                reply_content = ("欢迎参加全域科普活动，您的活动编码为 %03d ") % VAR.__seq__

        reply_xml = """
        <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime><![CDATA[%s]]></CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        </xml>"""%(toUser, fromUser, nowtime , reply_content)
        print('reply xml is %s', reply_xml)
        return HttpResponse(reply_xml)
    elif msgType == "event":
        
        event = str_xml.find('Event').text

        print("Event type is %s" %event )
        if event == "subscribe":
            print(" Even subscribe")
            fromUser = str_xml.find('ToUserName').text
            toUser = str_xml.find('FromUserName').text
            event = str_xml.find('Event').text
            nowtime = str(int(time.time()))
            
            reply_content = "等你好久了，欢迎关注\"天津科普说\"!点击链接开始测试你的科学素质水平https://pro.wenjuan.com/s2/5cb8128b7e634b22852f386b/"
            reply_xml = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime><![CDATA[%s]]></CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>"""%(toUser, fromUser, nowtime , reply_content)
            return HttpResponse(reply_xml)
        elif event == "CLICK":
            
            print("Click event")
            
            fromUser = str_xml.find('ToUserName').text
            toUser = str_xml.find('FromUserName').text
            event = str_xml.find('Event').text
            eventKey = str_xml.find('EventKey').text
            nowtime = str(int(time.time()))
            
            reply_content = "error"
            reply_xml = ""
            if (eventKey=="V2"):
                
                if toUser in VAR.user_dict:
                    number = VAR.user_dict[toUser]
                    print ("The user firs request for number %d "% number) 
                    reply_content = ("欢迎参加全域科普活动，您的活动编码为 %03d " % number)
                else:
                    VAR.__seq__ = VAR.__seq__+1
                    VAR.user_dict[toUser] = VAR.__seq__       
                    print("seq is %d " % VAR.__seq__)
                    reply_content = ("欢迎参加全域科普活动，您的活动编码为 %03d ") % VAR.__seq__

                reply_xml = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime><![CDATA[%s]]></CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>"""%(toUser, fromUser, nowtime , reply_content)
            return HttpResponse(reply_xml)

        # for the view or something else
        else:
            print("Other event")
            return HttpResponse()

class VAR:
    user_dict = {}
    __seq__ = 0

#https://pro.wenjuan.com/s2/5cb8128b7e634b22852f386b/
