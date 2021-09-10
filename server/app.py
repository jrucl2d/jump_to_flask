from flask import Flask, request
from flask_restx import Api, Resource
from todo.todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_namespace(Todo, '/todos')

@api.route('/hello/<string:name>')
class HelloWorld(Resource):
    def get(self, name):
        return {"hello": "world! %s" % name}
        
if __name__ == "__main__":
    app.run(debug=True, port= 8080)