from flask import request
from flask_restx import Resource, Namespace

Todo = Namespace('Todo')

todos = {}
count = 1

@Todo.route("")
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

@Todo.route("/<int:todo_id>")
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