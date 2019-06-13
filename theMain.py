from flask import Flask, request
import hashlib

app = Flask(__name__)


# for test the token from weixin
@app.route('/wx')
def hello_world():
	print(request)
	data = request.args
	print(data)
	#print(data['token'])
	#pri = web.input()
	if len(data) == 0 :
		return "wrong things"

	signature = data['signature']

	timestamp = data['timestamp']
	nonce = data['nonce']
	echostr = data['echostr']

	print("args is ", signature, timestamp, nonce, echostr)

	token = "123"
	list = [token, timestamp,nonce]
	list.sort()
	listStr = ''.join(list)

	sha1 = hashlib.sha1()
	#map(sha1.update, list)
	#hashcode = sha1.hexdigest()
	sha1.update(listStr.encode('utf-8'))
	hashcode = sha1.hexdigest()
	
	print ( "info is ", hashcode, signature)
	print("timestamp is" , timestamp)

	if hashcode == signature:
		return echostr
	else:
		return ""
