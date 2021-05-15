import pandas
import boto3

predictions = pd.DataFrame([[1,0,1,1,0,1,0,1,0,1,0,1,0,1]])

payload = predictions.to_json(orient="split")

result  = runtime.invoke_endpoint(EndpointName='pystock-api', Body=payload, ContentType='application/json')

preds = result['Body'].read().decode("ascii")

print(preds)
