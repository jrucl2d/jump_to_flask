from flask import Flask, request
from flask_restful import Resource, Api, abort, marshal_with
from todo_args import todo_post_args, todo_put_args
from todo_response import response, CustomResponse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {
            'hello' : 'world'
        }

todos = {}

def abort_func(todo_id):
    if todo_id not in todos:
        abort(404, message="Todo Id is not valid")

class TodoSimple(Resource):
    def get(self, todo_id):
        abort_func(todo_id)
        data = CustomResponse(todo_id, todos[todo_id])
        return data.to_response()
    def post(self, todo_id):
        # todos[todo_id] = request.form['data']
        args = todo_post_args.parse_args() # request를 parsing
        todos[todo_id] = args.id
        return {
            todo_id : todos[todo_id]
        }
    def put(self, todo_id):
        args = todo_put_args.parse_args()
        todos[todo_id] = args._id
        return {
            todo_id : todos[todo_id]
        }

class Todo1(Resource):
    def get(self):
        return {
            'task' : 'Hello World'
        }

class Todo2(Resource):
    def get(self):
        return {
            "task" : 'Hello World'
        }, 201

class Todo3(Resource):
    def get(self):
        return {
            'task' : 'Hello World'
        }, 201, {
            'Authorization' : 'some-token'
        }

api.add_resource(HelloWorld, "/")
api.add_resource(TodoSimple, "/<string:todo_id>")
api.add_resource(Todo1, "/todo/1")
api.add_resource(Todo2, "/todo/2")
api.add_resource(Todo3, "/todo/3")


if __name__ == '__main__':
    app.run(debug=True)