from google.cloud import bigquery
import pandas as pd     #conda install pandas-gbq -c conda-forge
from pandas.io import gbq
import os
#Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=725825577420-unm2gnkiprugilg743tkbig250f4sfsj.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fbigquery&state=k6pm2E0qGe0IENdbjWuF4bOAxc364H&prompt=consent&access_type=offline
#Enter the authorization code:4/1AX4XfWhcR9_IqzoIH0I309d0qnGYgQP2MXKf_JRpGg-UEkSMkm4CjF5M57A
#working code next 5 lines
query1="""SELECT * FROM `vn-project1.HealthCare_Data1.HC_StrokeData` LIMIT 100"""
#sqldata=gbq.read_gbq(query1, project_id="vn-project1")
#print(len(sqldata))
#sqldata.to_csv (r'C:\Users\Venu\Desktop\umich\CIS586-AdvanceDataManagement\project\export_dataframe.csv', index = False, header=True)
#sqldata.head(3)

# Dataframe to write
my_data = [{1,2,3}]
for i in range(0,10):
    my_data.append({i,2,3})
not_so_simple_dataframe = pd.DataFrame(data=my_data,columns=['a','b','c'])
print(my_data[5])

def str_to_date(str):
    return datetime.strptime(str, '%Y-%m-%d').date()

#print(str_to_date('12/13/2022'))


# df = pandas.DataFrame(
#         {
#             "my_string": ["a", "b", "c"],
#             "my_int64": [1, 2, 3],
#             "my_float64": [4.0, 5.0, 6.0],
#             "my_bool1": [True, False, True],
#             "my_bool2": [False, True, False],
#             "my_dates": pandas.date_range("now", periods=3),
#         }
#     )
#
# df=pd.read_gbq()

# creating a DataFrame
data = {
   'ID': [4],
   'Income': [10000],
   'Age': [19],
   'Profession': ['Pythoneer'],
   'Experience': [5],
   'Married_Single': ['Single'],
   'House_Ownership': ['owned'],
   'CITY': ['Canton'],
   'STATE': ['Michigan'],
   'CURRENT_JOB_YRS': [19],
   'CURRENT_HOUSE_YRS': [20],
}

df = pd.DataFrame(data)
print(df)
print('\n\n')

print('start')
query1="""SELECT * FROM `vn-project1.Credit.LoanData` LIMIT 1"""
#df=pd.read_gbq(query1, project_id="vn-project1")
print(df)

df.to_gbq(destination_table='Credit.LoanData', project_id='vn-project1', if_exists='append')
print('done')