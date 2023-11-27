## Transcription.py

Web-based transcription and summary service, designed to process and summarize text from various sources. Utilizing Flask, it offers a RESTful API endpoint that handles transcription and summarization requests.

### Usage

The application provides the following endpoints:

- `GET /`: A simple health check route that returns "Hello, World!".
- `POST /submit`: This endpoint accepts JSON data to process transcription and summarization using OAI API. It expects data in the format of SubmitRequest.

### Contributing
Contributions to this project are welcome. Please ensure to follow the project's coding standards and guidelines.