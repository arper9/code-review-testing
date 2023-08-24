

```
from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
  
@app.route('/hello', methods=['GET'])
def helloworld():
    """Returns 'Hello World' in a JSON response"""
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)
  
  
if __name__ == '__main__':
    app.run(debug=True)
