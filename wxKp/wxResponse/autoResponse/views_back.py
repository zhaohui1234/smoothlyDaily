from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import loader
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from lxml import etree
import time
from django.utils.encoding import smart_str


# store the user info 
user_dict = {}
__seq__ = 0

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
    fromUser = str_xml.find('ToUserName').text
    toUser = str_xml.find('FromUserName').text
    content = str_xml.find('Content').text
    nowtime = str(int(time.time()))

    if content != activity_name:
        reply_content = '欢迎参加全域科普活动，请您回复“全域科普”，获取活动编码'
    else:
        if fromUser in VAR.user_dict:
            number = VAR.user_dict[fromUser]
            print ("The user firs request for number %d "% number) 
            reply_content = ("您已经领取活动编码，您的活动编码为 %03d " % number)
        else:
            VAR.__seq__ = VAR.__seq__+1
            VAR.user_dict[fromUser] = VAR.__seq__       
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


class VAR:
    user_dict = {}
    __seq__ = 0

