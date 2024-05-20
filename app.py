from flask import Flask, request, jsonify, render_template
from google.cloud import storage
import os

app = Flask(__name__)

# Set up Google Cloud Storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloudstorageuploader-c9d203ce6c6e.json'
client = storage.Client()
bucket = client.get_bucket('bucket-quickstart_cloudstorageuploader')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return 'No file found', 400

    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)

    return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

'''from flask import Flask, request, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

# Set up Google Cloud Storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloudstorageuploader-c9d203ce6c6e.json'
client = storage.Client()
bucket = client.get_bucket('bucket-quickstart_cloudstorageuploader')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return 'No file found', 400

    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)

    return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)'''
