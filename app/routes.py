from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request


books_bp = Blueprint("books", __name__, url_prefix="/books")

# helper functions
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model


# route functions
@books_bp.route("", methods=["GET"])
def read_all_books():
    title_query = request.args.get("title")

    if title_query is not None:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    books_response = []     
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response), 200


# @books_bp.route("", methods=["POST"])
# def create_book():
#     if request.method == "POST":
#         request_body = request.get_json()
#         if "title" not in request_body or "description" not in request_body:
#             return make_response("Invalid Request", 400)

#         new_book = Book(
#             title = request_body["title"],
#             description = request_body["description"]
#         )

#         db.session.add(new_book)
#         db.session.commit()

#         return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)




@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)






@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_model(Book, book_id)

    return book.to_dict()

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(Book, book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    #return make_response(f"Book #{book_id} was successfully updated.")
    return make_response(jsonify(f"Book #{book_id} successfully updated"))

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    # return make_response(f"Book #{book_id} was successfully deleted.")
    return make_response(jsonify(f"Book #{book_id} successfully deleted"))




# REGISTERED FUNCTION TO RESPOND TO A ROUTE
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

