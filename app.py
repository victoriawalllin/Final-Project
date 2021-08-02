import pandas as pd
import pickle
from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS, cross_origin
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.metrics import mean_squared_error
from flask import Flask, render_template, request

# with open(f'victoria.pkl', 'rb') as f:
#     m = pickle.load(f)
# app = flask.Flask(__name__, template_folder='templates')
# @app.route('/')
# def main():
#     return(flask.render_template('main.html'))
# if __name__ == '__main__':
#     app.run()

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin()
def show_index.html():
    return render_template('form.html')

@app.route('/predict', methods = ['POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        form_data = request.form
        print(form_data)
        if 

if __name__ == '__main__':
    app.run(debbug=True)