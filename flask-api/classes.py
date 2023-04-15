from flask_restful import Resource, abort, reqparse, request
from init_db import connect_db

conn = connect_db()
cur = conn.cursor()


class HomeEndpoint(Resource):
    # Only accepts a get request
    def get(self):
        # Returns information about API with link to documentation
        return {
            "data":
            {
                "title": "Kiotapay API Test",
                'developer': "Collins Oden",
                "documentation": "https://github.com/collinsoden/kiotapay/README.md#usage"
            }
        }


class UserEndpoint(Resource):
    # Accepts post() and get() requests to save and return user data

    def get(self, user_id):
        # Get User Information from DB.
        try:
            cur.execute("SELECT * FROM users WHERE users.id = %s;", (user_id, ))
            userDetails = cur.fetchone()

            print(userDetails)
            # Close connections
            cur.close()
            conn.close()
        except Exception as e:
            return {
                "message": "We could not process your request"
            }, 500

        # End Process if user does not exist
        if userDetails == None:
            return {'message': 'We could not find the requested information, enter a valid ID'}

        return {
            "data": {
                "message": f"Bio Data for user with ID: `{user_id}` retrieved",
                "email": userDetails[1],
                "fullname": userDetails[2],
                "gender": userDetails[3],
                "age": userDetails[4],
                "status": userDetails[5]
            }
        }, 201

    def post(self):

        if request.method == 'POST':
            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument("email", type=str, help="Email address is required", location="json", required=True)
            user_post_args.add_argument("fullname", type=str, help="Full Name is required", location="json", required=True)
            user_post_args.add_argument("gender", type=str, help="Gender is required", location="json", required=True)
            user_post_args.add_argument("age", type=int, help="Age is required", location="json", required=True)

            args = user_post_args.parse_args()
            status = 'Active'

            print(args['fullname'])
            cur.execute("""INSERT INTO users (username, fullname, gender, age, status) VALUES (%s, %s, %s, %s, %s) RETURNING id;""", (args['email'], args['fullname'], args['gender'], args['age'], status))
            last_insert_id = cur.fetchone()[0]
            print(last_insert_id)

            cur.close()
            conn.close()

        else:
            return {
                "data": {
                    "message": "This Endpoint only recieves post request",
                    "user_link": "/api/v1/user/" # + user_id,
                }
        }, 300
        # Return Success Message if this information is saved, else "Error"
        return {
            "data": {
                "message": "User Information Saved",
                "user_link": f"/api/v1/user/{last_insert_id}",
            }
        }, 201

class TodoEndpoint(Resource):
    # Accepts post() and get() requests to save and return user data

    def get(self, todo_id):
        # Get User Information from DB.
    # Get User Information from DB.
        cur.execute(f"SELECT * FROM todos WHERE todos.id = {todo_id}")
        Todo = cur.fetchone()

        # Close connections
        cur.close()
        conn.close()
        # End Process if user does not exist
        if Todo == None:
            abort("We could not find the requested information, enter a valid ID")

        return {
            "data": {
                "message": f"Task with ID: `{todo_id}` retrieved",
                "email": Todo[1],
                "task": Todo[2],
                "status": Todo[3],
                "date_created": Todo[4]
            }
        }, 201


    def post(self, user_email):

        if request.method == 'POST':
            todo_post_args = reqparse.RequestParser()
            todo_post_args.add_argument("email", type=str, help="Email address is required", location="json", required=True)
            todo_post_args.add_argument("task", type=str, help="Task is required", location="json", required=True)

            args = todo_post_args.parse_args()
            status = 'Pending'
            last_insert_id = cur.execute("""INSERT INTO todos (username, task, status) VALUES (%s, %s, %s) RETURNING id;""", (args['email'], args['task'], status))

            print(last_insert_id)

            cur.close()
            conn.close()

        else:
            return {
                "data": {
                    "message": "This Endpoint only recieves post request",
                    "user_link": "/api/v1/todos/0"
                }
        }, 300
        # Return Success Message if this information is saved, else "Error"
        return {
            "data": {
                "message": "Todo Created",
                "user_link": f"/api/v1/todos/{last_insert_id}",
            }
        }, 201