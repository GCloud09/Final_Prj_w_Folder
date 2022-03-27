#import flask
from flask import Flask, render_template, request, redirect
from forms import RegistrationFormClass  #forms.py should be at root to identify this
# from typing import Dict
# from google.protobuf import json_format
# from google.protobuf.struct_pb2 import Value
# from google.cloud import aiplatform
# # If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# # called `app` in `main.py`.
#app = Flask(__name__)
app = Flask(__name__)  # template_folder='htmlfiles' path for templates folder should be above website
app.config['SECRET_KEY']='VenuAnishDeeptiInnisECE528CLOUDCOMPUTING'   #required for forms

@app.route('/')     #default page or route to different webpages
# display helloworld
def helloworld():
   return 'Credit Approval App'

# def indexpage():
#     return render_template('base.html')

@app.route('/test')
def root(): 
    return render_template('test.html') 

@app.route('/index')
def myindexpage():
    return render_template('index.html')   #file has to be in templates folder


@app.route('/registration', methods=['GET','POST'])  #to get formdata methods
def registration():
    form = RegistrationFormClass()
    if form.is_submitted():
        result = request.form
        successmsg="Your credit is approved"
        failuremsg="Your credit is declined"
        #set form elements to  ml model using variables
        checking_balance="1 - 200 DM"
        months_loan_duration= "20"
        credit_history= "fully repaid"
        purpose= "car (new)" 
        amount= form.amount.data #"4000" 
        savings_balance= "501 - 1000 DM"
        employment_length= "> 7 yrs"
        installment_rate= form.installment_rate.data
        personal_status= "married male"
        other_debtors= "guarantor"
        residence_history= "4"
        property= "real estate"
        age= form.age.data
        installment_plan= "bank"
        housing= "own"
        existing_credits= "1"
        default= "1"
        dependents= "1"
        telephone= form.telephone.data
        foreign_worker= form.telephone.data
        job= "skilled employee"        

        #run ml model here if we want
        # instance_dict={ "checking_balance": checking_balance, "months_loan_duration": "20", "credit_history": "fully repaid",
        #         "purpose": "car (new)", "amount": "4000", "savings_balance": "501 - 1000 DM",
        #         "employment_length": "> 7 yrs", "installment_rate": "4", "personal_status": "married male",
        #         "other_debtors": "guarantor", "residence_history": "4", "property": "real estate", "age": "25",
        #         "installment_plan": "bank", "housing": "own", "existing_credits": "1", "default": "1", "dependents": "1",
        #         "telephone": "yes", "foreign_worker": "yes", "job": "skilled employee"}

        instance_dict={ "checking_balance": checking_balance, "months_loan_duration": months_loan_duration, "credit_history": credit_history,
                "purpose": purpose, "amount": amount, "savings_balance": savings_balance,
                "employment_length": employment_length, "installment_rate": installment_rate, "personal_status": personal_status,
                "other_debtors": other_debtors, "residence_history": residence_history, "property": property, "age": age,
                "installment_plan": installment_plan, "housing": housing, "existing_credits": existing_credits, "default": default, "dependents": dependents,
                "telephone": telephone, "foreign_worker": foreign_worker, "job": job}
        # #call ml model using endpoints
        # location= "us-central1"
        # api_endpoint="us-central1-aiplatform.googleapis.com"
        # project="831128033926"
        # endpoint_id="5803213575308705792"
        # instance_dict=instance_dict
        #
        # # The AI Platform services require regional API endpoints.
        # client_options = {"api_endpoint": api_endpoint}
        # # Initialize client that will be used to create and send requests.
        # # This client only needs to be created once, and can be reused for multiple requests.
        # client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
        # # for more info on the instance schema, please use get_model_sample.py
        # # and look at the yaml found in instance_schema_uri
        # instance = json_format.ParseDict(instance_dict, Value())
        # instances = [instance]
        # parameters_dict = {}
        # parameters = json_format.ParseDict(parameters_dict, Value())
        # endpoint = client.endpoint_path(
        #     project=project, location=location, endpoint=endpoint_id
        # )
        # response = client.predict(
        #     endpoint=endpoint, instances=instances, parameters=parameters
        # )
        # print("response")
        # print(" deployed_model_id:", response.deployed_model_id)
        # # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
        # predictions = response.predictions
        # for prediction in predictions:
        #     print(" prediction:", dict(prediction))
        response='struct_value { fields { key: "classes" value { list_value { values { string_value: "1" } values { string_value: "2" } } } } fields { key: "scores" value { list_value { values { number_value: 0.5295441150665283 } values { number_value: 0.4704558551311493 } } } } } '
        predictions = response
        s = ""
        # for prediction in predictions:
        #     #s = s & dict(prediction)
        #     print(" prediction:", dict(prediction))
        # #deployed_model_id: "5384501955265560576" model: "projects/831128033926/locations/us-central1/models/2010685709806993408" model_display_name: "untitled_1645380369496_2022220212440""
        instances=""
        #response='response'
        return render_template('registrationsubmit.html',result=result, response1=response, response2=s, requestsent=instance_dict, response3=successmsg)
    return render_template('registration.html', form=form)

@app.route('/registration/<reg_id>')
def helloworld3(reg_id):
    return 'Credit Approval Registration Form ' + str(reg_id)

# @app.get("/")
# def hello():
#     """Return a friendly HTTP greeting."""
#     return "Hello World!\n"

app.run(port=8080, debug=True)

# if __name__ == "__main__":
#     # Used when running locally only. When deploying to Google App
#     # Engine, a webserver process such as Gunicorn will serve the app. This
#     # can be configured by adding an `entrypoint` to app.yaml.
#     app.run(host="localhost", port=8080, debug=True)






# def predict_tabular_classification_sample(
#     #project: str,
#     #endpoint_id: str,
#     #instance_dict: Dict,
#     location: str = "us-central1",
#     api_endpoint: str = "us-central1-aiplatform.googleapis.com",
#     project="831128033926",
#     endpoint_id="5803213575308705792",
#     instance_dict=instance_dict
# ):

    
    # # The AI Platform services require regional API endpoints.
    # client_options = {"api_endpoint": api_endpoint}
    # # Initialize client that will be used to create and send requests.
    # # This client only needs to be created once, and can be reused for multiple requests.
    # client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # # for more info on the instance schema, please use get_model_sample.py
    # # and look at the yaml found in instance_schema_uri
    # instance = json_format.ParseDict(instance_dict, Value())
    # instances = [instance]
    # parameters_dict = {}
    # parameters = json_format.ParseDict(parameters_dict, Value())
    # endpoint = client.endpoint_path(
    #     project=project, location=location, endpoint=endpoint_id
    # )
    # response = client.predict(
    #     endpoint=endpoint, instances=instances, parameters=parameters
    # )
    # print("response")
    # print(" deployed_model_id:", response.deployed_model_id)
    # # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
    # predictions = response.predictions
    # for prediction in predictions:
    #     print(" prediction:", dict(prediction))




