import requests
import json


appId = 'wx231e5484e2a44020' 

appSecret = '60dd9a3f7ce82607bde282ad4f45447e' 



def getToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, appSecret)
    result = requests.get(url)
    token = json.loads(result.text).get('access_token')
    print (token)
    return token
def main():
    token = getToken();
    url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token= %s' % token
    
    r= requests.get(url)
    print(r)
    print(r.text)
     




if __name__ == "__main__":
    main()




#://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN44020jjk44020jjk
