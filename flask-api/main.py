from flask import Flask
from flask_restful import Api, abort
from flask.views import MethodView


app = Flask(__name__)
api = Api(app)
BASE_URL = "/api/v1/"

# Import Resource Functions from functions.py
from classes import *

# API Index
api.add_resource(HomeEndpoint, BASE_URL, BASE_URL + '/home')
# UserEndpoint endpoint, user/<user_email> will return user details, matching specified email
api.add_resource(UserEndpoint, BASE_URL + '/user/<int:user_id>',
                 BASE_URL + '/user/', endpoint="user")
# TodoEndpoint todo/<req_id> will get todo with mathing id
api.add_resource(TodoEndpoint, BASE_URL + "/todos/<int:todo_id>",
                 BASE_URL + "/todo/", endpoint="todo")
if __name__ == __name__:
    app.run(debug=True, port=8000)