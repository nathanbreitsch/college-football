from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for


#import api
from api.quarterback import quarterback_api

app = Flask(__name__)

app.register_blueprint(quarterback_api)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
