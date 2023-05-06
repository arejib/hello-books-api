# from flask import Blueprint, jsonify, abort, make_response
# # jsonify get an array or somthing and turn it into json

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Book A", "Description A"),
#     Book(2, "Book B", "Description B"),
#     Book(3, "Book C", "Description C"),
#     ]

# # CREATED/REGISTERED BLUEPRINT
# books_bp = Blueprint("books", __name__, url_prefix="/books")

# def validate_book(book_id):
#     # handle invalid book_id
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     # search for book_id in data, return book
#     for book in books:
#         if book.id == book_id:
#              return book
        
#     # return 404 for non-existent book
#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# # REGISTERED FUNCTION TO RESPOND TO A ROUTE
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description,
#         })
#     return jsonify(books_response), 200

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }
    