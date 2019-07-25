import requests
import json



menu = {
    "button":[
        {
        "type":"view",
        "name":"快速监测",
        "url":"https://pro.wenjuan.com/s2/5cb8128b7e634b22852f386b/"
        },
        {
        "type":"click",
        "name":"获取抽奖码",
        "key":"V2"
        },
        {
        "type":"view",
        "name":"往期精彩",
        "url":"https://mp.weixin.qq.com/mp/homepage?__biz=MjM5ODIwOTQ5NQ==&hid=1&sn=87fa1cc92730ed7533285f0189ab0658"
        }
        ]
}



appId = 'wx231e5484e2a44020' 

appSecret = '60dd9a3f7ce82607bde282ad4f45447e' 



def getToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, appSecret)
    result = requests.get(url)
    print (result.text)
    token = json.loads(result.text).get('access_token')
    print (token)
    print (type(token))
    print('token is %s ' %token)
    return token
def main():
    data = json.dumps(menu,ensure_ascii=False).encode('utf-8')
    token = getToken();
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token= %s' % token
    
    r= requests.post(url, data)
    print(r)
    print(r.text)
     
if __name__ == "__main__":
    main()
