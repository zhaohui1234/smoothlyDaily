from django.shortcuts import render
from django.http import HttpResponse
import hashlib

def verify(request):
    
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
