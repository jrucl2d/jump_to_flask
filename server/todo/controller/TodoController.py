from flask import request
from flask_restx import Resource, Namespace, fields
from TodoDto import TodoRequest, TodoResponse

# Namespace를 따로 빼놓고 거기서 가져오는걸로
Todo = Namespace(
    name='Todo',
    description='Todo 리스트를 위한 api'    
)

class InnerVariables:
    count = 1
    todos = {}

@Todo.route("")
class TodoPost(Resource):
    @Todo.expect(TodoRequest) # body
    @Todo.response(201, 'Success', TodoResponse) # response
    def post(self):

        index = InnerVariables.count
        InnerVariables.count += 1
        InnerVariables.todos[index] = request.json.get('data')

        return {
            'todo_id' : index,
            'data' : InnerVariables.todos[index]
        }, 201

@Todo.route("/<int:todo_id>")
class TodoSimple(Resource):
    @Todo.response(200, 'Success', TodoResponse)
    @Todo.response(500, 'Failed')
    def get(self, todo_id):
        return {
            'todo_id' : todo_id,
            'data' : InnerVariables.todos[todo_id]
        }, 200
    
    @Todo.expect(TodoRequest)
    @Todo.response(202, 'Success', TodoResponse)
    @Todo.response(500, 'Failed')
    def put(self, todo_id):
        InnerVariables.todos[todo_id] = request.json.get('data')
        return {
            'todo_id' : todo_id,
            'data' : InnerVariables.todos[todo_id]
        }, 200

    @Todo.doc(responses={202: 'Success'})
    @Todo.doc(responses={500: 'Failed'})
    def delete(self, todo_id):
        del InnerVariables.todos[todo_id]
        return {
            "delete" : "success"
        }, 200