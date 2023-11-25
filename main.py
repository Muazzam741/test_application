import json
from fastapi import FastAPI, HTTPException
import boto3

app = FastAPI()
aws_region = 'ap-south-1'
table_name = 'QueueStatus'
aws_access_key_id = ''
aws_secret_access_key = ''

dynamodb = boto3.resource('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
table = dynamodb.Table(table_name)

@app.get("/queuestatus")
async def get_all_items():
    try:
        response = table.scan()
        items = response.get('Items', [])
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
