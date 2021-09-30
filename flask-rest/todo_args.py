from flask_restful import reqparse

todo_post_args = reqparse.RequestParser()
todo_post_args.add_argument("id", type=str, help="Post Args")

todo_put_args = reqparse.RequestParser()
todo_put_args.add_argument("_id", type=str, help="Put Args")