import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/"
headers = {'accept': 'application/json'}


# Request API Info:: Done Working, Uncomment to text api
# response = requests.get(BASE_URL)
# print(response.json())


# Request User Info: Uncomment below to get user data
# user_id = 1 # User id to find
# response = requests.get(BASE_URL + f"user/{user_id}")
# print(response.json())


# Save User Information, Uncomment add add your details to create user
user_data = {
    "email": "collinsoden22@gmail.com",
    "fullname": "Collins Oden",
    "gender": "Male",
    "age": "23"
}

response = requests.post(BASE_URL + "user/0", json=user_data)
print(response.json())
