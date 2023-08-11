from flask import Flask, request, jsonify, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    try:
        # Get the image file from the POST request
        image_file = request.files.get('image')

        if image_file is None:
            return jsonify({'error': 'No image file provided'}), 400

        # Load the image using PIL
        image = Image.open(image_file)

        # Remove background using rembg
        output = remove(image)

        # Create a response with the processed image
        output_buffer = io.BytesIO()
        output.save(output_buffer, format='PNG')
        output_buffer.seek(0)

        return send_file(output_buffer, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
