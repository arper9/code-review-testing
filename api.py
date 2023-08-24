 
from google.cloud import storage
from flask import Flask, jsonify

app = Flask(__name__)

# Return a JSON response containing a 'Hello World' message
@app.route('/hello', methods=['GET'])
def helloworld():
    # Create a dictionary containing the response data
    response = {
        'message': 'Hello World'
    }
    # Return the response data in a JSON format
    return jsonify(response)
  
if __name__ == '__main__':
    app.run(debug=False)
