import pymongo
from flask import Flask
from flask import request
from flask import json
from uuid import uuid4

app = Flask(__name__)

client = pymongo.MongoClient(<MONGOURL>)
db = client.FlaskWorkshop

@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    if request.method == 'POST':
        id = str(uuid4()).replace('-', '')
        userData = request.get_json()
        userData['_id'] = id
        doc = db['users'].insert_one(userData)
        if doc == None:
            return json.jsonify({
                'error': 'Some server error occured'
            }), 500
        else:
            return json.jsonify({
                'status': True,
            }), 200
    elif request.method == 'GET':
        query = request.args
        doc = db['users'].find_one({
            '_id': query['id']
        })
        if doc == None:
            return json.jsonify({
                'error': 'User not found'
            }), 404
        else:
            return json.jsonify(doc), 200
    elif request.method == 'DELETE':
        query = request.args
        doc = db['users'].find_one({
            '_id': query['id']
        })
        if doc != None:
            dele = db['users'].delete_one({
                '_id': query['id']
            })
            return json.jsonify({
                'status': True
            }), 200
        else: 
            return json.jsonify({
                'error': 'User not found'
            }), 404
    elif request.method == 'PATCH':
        query = request.args
        data = request.get_json()
        doc = db['users'].find_one({
            '_id': query['id']
        })
        if doc != None:
            db['users'].update_one({
                '_id': query['id']
            }, {
                '$set': data
            })
            return json.jsonify({
                'status': True,
            }), 200
        else:
            return json.jsonify({
                'error': 'User not found'
            }), 404
            

@app.route('/user/<id>')
def getUser(id):
    doc = db['users'].find_one({
        '_id': id
    })
    if doc == None:
        return json.jsonify({
            'error': 'User doesn\'t exist' 
        }), 404
    else:
        return json.jsonify(doc), 200


@app.route('/list')
def getList():
    doc = list(db['users'].find())
    return json.jsonify(doc), 200

if __name__ == "__main__":
    app.run(debug=True)
