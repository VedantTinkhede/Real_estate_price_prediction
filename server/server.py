from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/get_location_names')
def get_location_names():
    # This function would typically fetch location names from columns_names
    # For demonstration, we return a static list 
    response = jsonify({
        'locations': util.get_location_names()
    })   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting the Flask server...")
    util.load_saved_artifacts()  # Load the model and data columns before starting the server
    app.run()