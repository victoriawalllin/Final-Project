from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS, cross_origin
import joblib
import pandas as pd

# Create an instance of Flask
app = Flask(__name__)
cors = CORS(app)

m = joblib.load('victoria.pkl')



# Route to render index.html template using data from Mongo
@app.route("/")
@cross_origin()
def home():
    # Find one record of data from the mongo database

    # Return template and data
    return render_template("form.html")

# Route that will trigger the scrape function
@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        prd = pd.DataFrame({
            "neighbourhood" : [form_data["neighbourhoodchoice"]],
            "room_type":[form_data["roomchoice"]],
            "minimum_nights" : [form_data["Minimum Nights"]],
            "number_of_reviews" : [form_data["Number of Reviews"]],
            "reviews_per_month":[form_data["Reviews per month"]],
            "availability_365": [form_data["Days Available out of the Year"]]
})
        # do more calculations here with the input data which is
        # in the form_data dictionary
        letter = m.predict(prd)
        return render_template('predict.html', form=form_data, letter=letter)


if __name__ == "__main__":
    app.run(debug=True)