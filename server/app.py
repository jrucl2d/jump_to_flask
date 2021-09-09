from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}
count = 1

@api.route("/todos")
class TodoPost(Resource):
    def post(self):
        global count
        global todos

        index = count
        count += 1
        todos[index] = request.json.get('data')

        return {
            'todo_id' : index,
            'data' : todos[index]
        }

@api.route("/todos/<int:todo_id>")
class TodoSimple(Resource):
    def get(self, todo_id):
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }
    
    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }

    def delete(self, todo_id):
        del todos[todo_id]
        return {
            "delete" : "success"
        }

@api.route('/hello/<string:name>')
class HelloWorld(Resource):
    def get(self, name):
        return {"hello": "world! %s" % name}
        
if __name__ == "__main__":
    app.run(debug=True, port= 8080)