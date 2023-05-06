# from flask import Blueprint, jsonify
# # jsonify get an array or somthing and turn it into json

# # CREATED/REGISTERED BLUEPRINT
# hello_world_bp = Blueprint("hello_world", __name__)

# # define endpoint; only responds to GET requests
# # user hello_world_bp for the /hello_world route on GET requests...
# # ...calls the function
# # REGISTERED FUNCTION TO RESPOND TO A ROUTE
# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body, 200


# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }, 200


# # BROKEN COMMENTED OUT
# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     #response_body["hobbies"] + new_hobby
#     response_body["hobbies"].append(new_hobby)
#     return response_body