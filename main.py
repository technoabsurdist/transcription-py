from flask import Flask, request, jsonify
from models import SubmitRequest, SubmitResponse
from transcripter import transcription 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/submit', methods=['POST'])
def handle_submit():
    try:
        data = SubmitRequest(**request.json)
    except ValueError as e:
        return str(e), 400

    text, metadata = transcription(data.url)
    response = SubmitResponse(
        title=metadata['title'],
        thumbnail_url=metadata['thumbnail_url'],
        author=metadata['author'],
        text=text
    )
    return jsonify(response.model_dump())

if __name__ == '__main__':
    app.run(debug=True)
