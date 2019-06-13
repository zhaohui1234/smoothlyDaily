from flask import Flask, request

app = Flask(__name__)


# for test the token from weixin
@app.route('/wx')
def hello_world():
        print(request)
        data = request.args
        print(data)
        #print(data['token'])

        #print(request.name)
        return 'Hello, World!'

#if __name__ == "__main__":
#    app.run()
