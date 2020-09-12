from flask import Flask, request

from greet import greet

app = Flask(__name__)

@app.route('/')
def main():
    ip_address = request.headers['X-Forwarded-For']
    print(ip_address)
    print(request.headers)
    return greet(ip_address)
    

@app.route('/bye')
def bye():
    return "Adios!"


@app.route('/ask')
def ask():
    return "How are you doing"


if __name__ == '__main__':
    app.run()
