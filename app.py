from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle thumbnail requests
@app.route('/get-thumbnail', methods=['GET'])
def get_thumbnail():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400

    # Construct the URL for the max resolution thumbnail
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    # Fetch the thumbnail
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        return response.content, 200, {'Content-Type': 'image/jpeg'}
    else:
        return jsonify({"error": "Thumbnail not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
