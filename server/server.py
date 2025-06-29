from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = request.form['total_sqft']
    location = request.form['location']
    bath = request.form['bath']
    bhk = request.form['bhk']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    util.load_saved_artifacts()
    print("Starting Flask server...")
    app.run()