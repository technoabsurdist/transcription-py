from flask import Flask, request, jsonify
from models import SubmitRequest, SubmitResponse
from helpers import transcription, generate_summary
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/submit": {"origins": "https://transcript-fe.vercel.app"}})

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/submit', methods=['POST'])
@cross_origin(origin='https://transcript-fe.vercel.app', headers=['Content- Type', 'Authorization'])
def handle_submit():
    try:
        data = SubmitRequest(**request.json)
    except ValueError as e:
        return str(e), 400

    text, metadata = transcription(data.url)
    summary = generate_summary(text)
    response = SubmitResponse(
        title=metadata['title'],
        thumbnail_url=metadata['thumbnail_url'],
        author=metadata['author'],
        text=text,
        summary=summary
    )
    response.headers['Access-Control-Allow-Origin'] = 'https://transcript-fe.vercel.app'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return jsonify(response.model_dump())

if __name__ == '__main__':
    app.run(debug=True)
