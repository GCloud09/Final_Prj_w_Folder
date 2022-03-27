#pip install flask, flask-WTF
# pypi.org packages for python. File -->settings--> interpreter

from flask import Flask, render_template, request, redirect
from forms import RegistrationFormClass
from google.cloud import bigquery
import pandas as pd     #conda install pandas-gbq -c conda-forge
from pandas.io import gbq
import os

app = Flask(__name__)   #new instance of the app
app.config['SECRET_KEY']='VenuAnishDeeptiECE528CLOUDCOMPUTING'   #required for forms
@app.route('/')     #default page or route to different webpages
# display helloworld
#def helloworld():
#    return 'Credit Approval App'
def indexpage():
    return render_template('base.html')

@app.route('/index')
def myindexpage():
    return render_template('index.html')   #file has to be in templates folder

@app.route('/contact')
def mycontactpage():
    return render_template('contact.html')   #file has to be in templates folder

@app.route('/registration', methods=['GET','POST'])  #to get formdata methods
def registration():
    form = RegistrationFormClass()
    if form.is_submitted():
        result = request.form
        successmsg="Your credit is approved"
        failuremsg='Your credit is declined'
        #call ml model using endpoints
        #predict_tabular_classification_sample(
            project="831128033926"
            endpoint_id="5803213575308705792"
            location="us-central1"
           # instances=[{"feature_column_a": "value", "feature_column_b": "value"...}, {...}]
        #)
        #run ml model here if we want
        return render_template('registrationsubmit.html',result=result, response1=successmsg, response2=failuremsg)
    return render_template('registration.html', form=form)

@app.route('/registration/<reg_id>')
def helloworld3(reg_id):
    return 'Credit Approval Registration Form ' + str(reg_id)
# keep this
if __name__ == '__main__':
    app.run()
