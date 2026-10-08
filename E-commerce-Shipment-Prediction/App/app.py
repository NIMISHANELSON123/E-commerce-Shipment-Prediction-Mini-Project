from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        warehouse_block = request.form.get('Warehouse_block', 'A')
        mode_of_shipment = request.form.get('Mode_of_Shipment', 'Flight')
        customer_care_calls = float(request.form.get('Customer_care_calls', 0))
        customer_rating = float(request.form.get('Customer_rating', 0))
        cost_of_the_product = float(request.form.get('Cost_of_the_Product', 0))
        prior_purchases = float(request.form.get('Prior_purchases', 0))
        product_importance = float(request.form.get('Product_importance', 1))
        gender = request.form.get('Gender', 'F')
        discount_offered = float(request.form.get('Discount_offered', 0))
        weight_in_gms = float(request.form.get('Weight_in_gms', 0))
        
        # Calls_Per_Purchase 
        calls_per_purchase = customer_care_calls / (prior_purchases + 1)
        
        
        features = np.array([[
            7500,  # ID placeholder
            customer_care_calls,
            customer_rating,
            cost_of_the_product,
            prior_purchases,
            product_importance,
            discount_offered,
            weight_in_gms,
            calls_per_purchase,
            1 if warehouse_block == 'B' else 0,
            1 if warehouse_block == 'C' else 0,
            1 if warehouse_block == 'D' else 0,
            1 if warehouse_block == 'F' else 0,
            1 if mode_of_shipment == 'Road' else 0,
            1 if mode_of_shipment == 'Ship' else 0,
            1 if gender == 'M' else 0
        ]])
        
        # Make prediction
        prediction = model.predict(features)
        output = prediction[0]
        
        if output == 1:
            result_text = "The shipment will be delayed."
        else:
            result_text = "The shipment will reach on time."
            
        return render_template('index.html', prediction_text=result_text)
        
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)