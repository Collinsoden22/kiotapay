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


# Accepts post() and get() requests to save and return user data
class UserEndpoint(Resource):

    def get(self, user_id):
        self.cur, self.conn = cur, conn

        try:
            # Get User Information from DB.
            self.cur.execute(
                "SELECT * FROM users WHERE users.id = %s;", (user_id, ))
            userDetails = self.cur.fetchone()

        except Exception as e:
            return {
                "message": "We could not process your request",
                "error": str(e)
            }, 500

        # Close connections
        cur.close()
        conn.close()
        # End Process if user does not exist
        if userDetails == None:
            return {
                "message": f"We could not find the requested information, enter a valid ID: {user_id}"
            }, 404

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
            user_post_args.add_argument(
                "email", type=str, help="Email address is required", location="json", required=True)
            user_post_args.add_argument(
                "fullname", type=str, help="Full Name is required", location="json", required=True)
            user_post_args.add_argument(
                "gender", type=str, help="Gender is required", location="json", required=True)
            user_post_args.add_argument(
                "age", type=int, help="Age is required", location="json", required=True)

            args = user_post_args.parse_args()
            status = 'Active'
            try:
                insert_user = "INSERT INTO users (username, fullname, gender, age, status) VALUES (%s, %s, %s, %s, %s) RETURNING id;"
                cur.execute(
                    insert_user, (args['email'], args['fullname'], args['gender'], args['age'], status, ))
                conn.commit()
            except Exception as e:
                conn.rollback()
                return {
                    "data": {
                        "message": "We could not complete your request",
                        "error": str(e)
                    }
                }, 500

            last_insert_id = cur.fetchone()[0]

            cur.close()
            conn.close()

        else:
            return {
                "data": {
                    "message": "This Endpoint only recieves post request",
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
        self.cur, self.conn = cur, conn
       # Get User Information from DB.
       # Get User Information from DB.
        try:
            # Get User Information from DB.
            self.cur.execute(
                "SELECT * FROM todos WHERE todos.id = %s;", (todo_id, ))
            Todo = self.cur.fetchone()

        except Exception as e:
            return {
                "message": "We could not process your request",
                "error": str(e)
            }, 500

        # Close connections
        cur.close()
        conn.close()

        if Todo == None:
            abort("We could not find the requested information, enter a valid ID")

        return {
            "data": {
                "message": f"Task with ID: `{todo_id}` retrieved",
                "email": Todo[1],
                "task": Todo[2],
                "status": Todo[3],
                # "date_created": Todo[4]
            }
        }, 201

    def post(self):

        if request.method == 'POST':
            todo_post_args = reqparse.RequestParser()
            todo_post_args.add_argument(
                "email", type=str, help="Email address is required", location="json", required=True)
            todo_post_args.add_argument(
                "task", type=str, help="Task is required", location="json", required=True)

            args = todo_post_args.parse_args()
            status = 'Pending'
            try:
                cur.execute(
                    "INSERT INTO todos (username, task, status) VALUES (%s, %s, %s) RETURNING id;", (args['email'], args['task'], status))

                conn.commit()
            except Exception as e:
                conn.rollback()
                return {
                    "data": {
                        "message": "We could not save todo data",
                        "error": str(e)
                    }
                }, 500

            last_insert_id = cur.fetchone()[0]
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
                "user_link": "/api/v1/todos/" + str(last_insert_id)
            }
        }, 201
