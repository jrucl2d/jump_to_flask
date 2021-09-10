from flask_restx import fields
from .TodoController import Todo

TodoRequest = Todo.model('TodoRequest', {
'data' : fields.String(description='Todo 데이터', required=True, example='What to do')
})

TodoResponse = Todo.inherit('TodoResponse', TodoRequest, {
    'id' : fields.Integer(description='Todo 아이디')
})