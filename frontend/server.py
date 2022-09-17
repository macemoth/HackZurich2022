from flask import Flask, jsonify, render_template, request
import json
from search import Search

server = Flask(__name__)
server.config.update(SERVER_NAME='127.0.0.1:5000')
search = Search()

@server.route('/')
def index():
    return render_template('index.html')

# @server.route('/search/<query>')
# def search(query):
#     params = query.split("&")
#     print(params)
#     # results = search.search(params)
#     # return jsonify(results)

@server.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    return render_template('results.html')
    # return render_template('results.html', res=res )

@server.route('/suggestions/<prefix>')
def get_suggestions(prefix):
    return jsonify(search.get_suggestions(prefix))