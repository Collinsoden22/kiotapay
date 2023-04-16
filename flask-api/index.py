from flask import Flask
from flask_restful import Api, abort
from flask.views import MethodView


app = Flask(__name__)
api = Api(app)
BASE_URL = "/api/v1/"

from classes import *

# API Index
api.add_resource(HomeEndpoint, BASE_URL, BASE_URL + '/home')
api.add_resource(UserEndpoint, BASE_URL + '/user/<int:user_id>',
                 BASE_URL + '/user/', endpoint="user")
# TodoEndpoint todo/<req_id> will get todo with mathing id
api.add_resource(TodoEndpoint, BASE_URL + "/todos/<int:todo_id>",
                 BASE_URL + "/todos/", endpoint="todos")
api.add_resource(FetchAllTodoEndpoint, BASE_URL +
                 "/todo/<user>", endpoint="todo")
if __name__ == __name__:
    app.run(debug=True, port=8000)