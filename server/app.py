from flask import Flask
from flask_restx import Api, Resource
from todo.controller.TodoController import Todo

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='flask server',
    description='플라스크 공부용 서버',
    terms_url='/',
    contact='ysk789465@gmail.com',
    license='MIT'
)

api.add_namespace(Todo, '/todos')

@api.route('/hello/<string:name>')
class HelloWorld(Resource):
    def get(self, name):
        return {"hello": "world! %s" % name}
        
if __name__ == "__main__":
    app.run(debug=True, port= 8080)