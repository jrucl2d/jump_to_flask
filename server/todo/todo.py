from flask import request
from flask_restx import Resource, Namespace, fields

Todo = Namespace(
    name='Todo',
    description='Todo 리스트를 위한 api'    
)

todo_fields = Todo.model('Todo', {
    'data' : fields.String(description='a Todo', required=True, example='What to do')
})

todo_fields_with_id = Todo.inherit('Todo With ID', todo_fields, {
    'id' : fields.Integer(description='a Todo ID')
})

todos = {}
count = 1

@Todo.route("")
class TodoPost(Resource):
    @Todo.expect(todo_fields) # body
    @Todo.response(201, 'Success', todo_fields_with_id) # response
    def post(self):
        global count
        global todos

        index = count
        count += 1
        todos[index] = request.json.get('data')

        return {
            'todo_id' : index,
            'data' : todos[index]
        }, 201

@Todo.route("/<int:todo_id>")
class TodoSimple(Resource):
    @Todo.response(200, 'Success', todo_fields_with_id)
    @Todo.response(500, 'Failed')
    def get(self, todo_id):
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }, 200
    
    @Todo.response(202, 'Success', todo_fields_with_id)
    @Todo.response(500, 'Failed')
    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id' : todo_id,
            'data' : todos[todo_id]
        }, 200

    @Todo.doc(responses={202: 'Success'})
    @Todo.doc(responses={500: 'Failed'})
    def delete(self, todo_id):
        del todos[todo_id]
        return {
            "delete" : "success"
        }, 200