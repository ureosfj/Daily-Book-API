from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le origini su tutte le rotte

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"
    
with app.app_context():
    db.create_all()
@app.route('/api/add-book', methods=['POST'])
def add_book():
    if not request.json:
        abort(400)  # abort if no JSON data is received
    if 'title' not in request.json or 'author' not in request.json:
        abort(400)  # abort if essential book information is missing
    
    new_book = Book(
        title=request.json['title'],
        author=request.json['author'],
        genre=request.json.get('genre', 'Not specified'),  # default genre if not specified
        summary=request.json.get('summary', '')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/')
def home():
    return "Benvenuto alla API Libro del Giorno!"

@app.route('/api/book-of-the-day')
def book_of_the_day():
    book = Book.query.order_by(db.func.random()).first()
    return jsonify({'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary})

@app.route('/api/search')
def search_books():
    genre = request.args.get('genre')
    found_books = Book.query.filter(Book.genre.ilike(f"%{genre}%")).all()
    results = [{'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary} for book in found_books]
    return jsonify(results)

@app.route('/api/recommendations')
def recommendations():
    # Simulazione semplice: restituisce un libro random non basato sull'utente
    book = Book.query.order_by(db.func.random()).first()
    return jsonify({'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary})

@app.route('/api/all')
def history():
    all_books = Book.query.all()
    results = [{'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary} for book in all_books]
    return jsonify(results)


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.summary = data.get('summary', book.summary)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

@app.route('/api/search', methods=['GET'])
def advanced_search():
    query = Book.query
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if author:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    if genre:
        query = query.filter(Book.genre.ilike(f'%{genre}%'))

    books = query.all()
    results = [{'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary} for book in books]
    return jsonify(results)

@app.route('/api/books/genre/<genre_name>', methods=['GET'])
def list_books_by_genre(genre_name):
    books = Book.query.filter(Book.genre.ilike(f'%{genre_name}%')).all()
    results = [{'id': book.id, 'title': book.title, 'author': book.author, 'summary': book.summary} for book in books]
    return jsonify(results)

@app.route('/api/stats', methods=['GET'])
def books_stats():
    total_books = Book.query.count()
    books_by_genre = db.session.query(Book.genre, db.func.count(Book.genre)).group_by(Book.genre).all()
    stats = {
        'total_books': total_books,
        'books_by_genre': {genre: count for genre, count in books_by_genre}
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
