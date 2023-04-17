import requests

BASE_URL = "https://flask-qmtq2b0vu-collinsoden22.vercel.app/api/v1/"
headers = {'accept': 'application/json'}


# TODO  Request API Info:: Done Working, Uncomment to text api
# response = requests.get(BASE_URL)
# print(response.json())


# TODO  Request User Info: Uncomment below to get user data
# user_id = 1  # User id to find
# response = requests.get(BASE_URL + "user/{}".format(user_id))
# print(response.json())


# TODO  Save User Information, Uncomment add add your details to create user
# user_data = {
#     "email": "example@gmail.com",
#     "fullname": "John Doe",
#     "gender": "Male",
#     "age": "33"
# }

# response = requests.post(BASE_URL + "user/", json=user_data)
# print(response.json())


# TODO Request Todo Info: Uncomment below to get todo
# task_id = 1  # Task id to find
# response = requests.get(BASE_URL + f"todos/{task_id}")
# print(response.json())


# TODO Save User Information, Uncomment add add your details to create user
# user_data = {
#     "email": "example@gmail.com",
#     "task": "Get grocceries later"
# }

# response = requests.post(BASE_URL + "todo", json=user_data)
# print(response.json())


# TODO Get all tasks for specifed user
# email = example@gmail.com  # User id to find
# response = requests.get(BASE_URL + f"todo/{email}")
# print(response.json())
