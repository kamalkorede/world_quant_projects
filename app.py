import os

from flask import Flask, request

from greet import greet, get_ip_address

DEPLOY = os.environ.get('DEPLOY')

app = Flask(__name__)


@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = get_ip_address()

    return greet(ip_address)
    

@app.route('/bye')
def bye():
    return "Adios!"


@app.route('/ask')
def ask():
    return "How are you doing today?"


if __name__ == '__main__':
    app.run()
