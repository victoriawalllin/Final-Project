import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import mean_squared_error
from flask import Flask, render_template, request

with open(f'victoria.pkl', 'rb') as f:
    m = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run()

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index.html():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        print ("Pay is " + pay)
        return "Data sent. Please check your program log"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debbug=True)