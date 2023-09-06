from flask import Flask, jsonify

# Create a Flask web application
app = Flask(__name__)

# Define a sample endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)
