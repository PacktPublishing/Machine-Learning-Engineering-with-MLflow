import pandas as pd
import boto3

predictions = pd.DataFrame([[1,0,1,1,0,1,0,1,0,1,0,1,0,1]])

payload = predictions.to_json(orient="split")

runtime = boto3.client('sagemaker-runtime')

result  = runtime.invoke_endpoint(EndpointName='pystock-api', Body=payload, ContentType='application/json')

preds = result['Body'].read().decode("ascii")

print(preds)
