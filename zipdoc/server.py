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
    search_query = request.form["input"]
    if len(search_query.split(" ")) == 0:
        return index()
    
    hits, summaries, similars = search.search(search_query)
    response = {"hits": hits, "summaries": summaries, "similars": similars}
    # return render_template('results.html')
    return render_template('results.html', res=response)
