from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for books
books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    books.append(data)
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books/<int:index>', methods=['DELETE'])
def remove_book(index):
    if index < len(books):
        del books[index]
        return jsonify({'message': 'Book removed successfully'}), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
