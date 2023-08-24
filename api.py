

```
from flask import Flask, jsonify
  
app = Flask(__name__)
  
# Returns 'Hello World' in a JSON response
@app.route('/hello', methods=['GET'])
def helloworld():
    data = {'data': 'Hello World'}
    return jsonify(data)
  
  
if __name__ == '__main__':
    app.run(debug=True)
