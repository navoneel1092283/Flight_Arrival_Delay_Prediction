import urllib
# If you are using Python 3+, import urllib instead of urllib2 
import json 
 
data = { 
        "Inputs": { 
                "input1": 
                [ 
                    { 
                            'Year': "1",    
                            'Month': "1",    
                            'DayofMonth': "1",    
                            'DayOfWeek': "1",    
                            'Carrier': "",    
                            'OriginAirportID': "1",    
                            'DestAirportID': "1",    
                             

 
 
                          
                            'CRSDepTime': "1",    
                            'CRSArrTime': "1",    
                            'Year (2)': "1",    
                            'Timezone': "1",    
                            'Visibility': "1",    
                            'DryBulbFarenheit': "1",    
                            'DryBulbCelsius': "1",    
                            'DewPointFarenheit': "1",    
                            'DewPointCelsius': "1",    
                            'RelativeHumidity': "1",    
                            'WindSpeed': "1",    
                            'Altimeter': "1",    
                            'Year (3)': "1",    
                            'Timezone (2)': "1",    
                            'Visibility (2)': "1",    
                            'DryBulbFarenheit (2)': "1",    
                            'DryBulbCelsius (2)': "1",    
                            'DewPointFarenheit (2)': "1",    
                            'DewPointCelsius (2)': "1",    
                            'RelativeHumidity (2)': "1",    
                            'WindSpeed (2)': "1",    
                            'Altimeter (2)': "1",    
                    } 
                ], 
        }, 
    "GlobalParameters":  { 
    } 
} 
 
body = str.encode(json.dumps(data)) 
 
 
 

 
 
url='https://ussouthcentral.services.azureml.net/workspaces/5901f903e459409ba44bc70c3c63b07a/services/8291041561294af8adddd2a9928bb784/execute?apiversion=2.0&format=swagger' 
 
 
 
api_key='629KgGTHKGDjYJBGNLXDJoStxs0SLS6D+VBCAE8KZlq/zoxt/weh9oIQBfv039mEuyM+vmsrkKqa0pH8cCD5kQ==' # Replace this with the API key for the web service 
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)} 
 
req = urllib.Request(url, body, headers) 
 
try: 
    response = urllib.urlopen(req) 
# If you are using Python 3+, replace urllib2 with urllib.request in the above code: 
# req = urllib.request.Request(url, body, headers) 
# response = urllib.request.urlopen(req) 
 
    result = response.read() 
    print(result) 
except urllib.HTTPError,error: 
    print("The request failed with status code: " + str(error.code)) 
 
    # Print the headers - they include the requert ID and the timestamp, which are useful for 
debugging the failure 
    print(error.info()) 
    print(json.loads(error.read()))  
