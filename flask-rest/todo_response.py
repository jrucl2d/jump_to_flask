from flask_restful import fields

response = {
    'id' : fields.String,
    'todo' : fields.String
}

class CustomResponse:
    def __init__(self, id, todo):
        self._id = id
        self._todo = todo
    
    def to_response(self):
        return {
            "id" : self._id,
            "todo" : self._todo
        }