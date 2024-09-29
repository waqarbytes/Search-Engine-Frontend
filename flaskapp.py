from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://search-engine-backend2.onrender.com"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    search_term = request.args.get('q')
    # Imagine we fetch results from different APIs here
    results = [
        {'title': 'YouTube Video', 'description': 'A great video', 'link': 'https://youtube.com'},
        {'title': 'Research Paper', 'description': 'An interesting paper', 'link': 'https://scholar.google.com'},
    ]
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
