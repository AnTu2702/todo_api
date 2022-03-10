import os, json, boto3

from botocore.exceptions import ClientError

### REMARK: I would normally use a schema validation to stay flexible, but for this simple...
### ...demo task, I did not want to invest more effort on importing 3rd-party-libs into lambda.
### In addtion the schema given in the openapi file is (intentionally?!) broken.
### So this hint seems suffient for now, instead of fixing the world...

def respond(err, res=None):

    response =  {
            "statusCode": 200 if err is None else err ,
            "body": json.dumps(res),
            "headers": { "Content Type": "application/json",
                         "Access-Control-Allow-Headers" : "Content-Type",
                         "Access-Control-Allow-Origin": "https://editor.swagger.io",
                         "Access-Control-Allow-Methods": "OPTIONS,GET,PUT,DELETE" },
            "isBase64Encoded": False
        }
    
    print(f"Response on event: {response}")
    return response
    
def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    table = client.Table(os.environ.get("TODO_DYNAMODB_TABLE"))
    
    print(f"Received event: {json.dumps(event, indent=2)}")
    
    try:

        if event['requestContext']['resourcePath'] == '/v1/todo/{todo_id}' and event['httpMethod'] == 'DELETE':
    
            try:
                response = table.delete_item(Key={'id': event['pathParameters']['todo_id']}, ConditionExpression='attribute_exists(id)')
            except ClientError as e:
                return respond(400, {"error": "There has been an error while deleting the ToDo object."})
            else:
                return respond(None, {"message": "ToDo object deleted successfully."})
            
        elif event['requestContext']['resourcePath'] == '/v1/todo/{todo_id}' and event['httpMethod'] == 'PUT':
            
            body = json.loads(event['body'])
            
            try:
                if event['pathParameters']['todo_id'] == body['id']:
                    response = table.put_item(Item={'id': body['id'], 'title': body['title'], 'description': body['description']}, ConditionExpression='attribute_exists(id)')
                else:
                    raise ClientError({},"")
            except ClientError as e:
                return respond(400, {"error": "There was an error while creating a new ToDo object."})
            else:
                return respond(None, {"message": "ToDo object created successfully."})
    
    
        elif event['requestContext']['resourcePath'] == "/v1/todo/{todo_id}" and event['httpMethod'] == 'GET':
            
            try:
                response = table.get_item(Key={'id': event['pathParameters']['todo_id']})
            except ClientError as e:
                return respond(400, {"error": "There was an error loading the ToDo objects."})
            else:
                return respond(None, [response['Item']]) if 'Item' in response else respond(400, {"error": "There was an error loading the ToDo objects."})
       
        elif event['requestContext']['resourcePath'] == "/v1/todo" and event['httpMethod'] == 'GET':
            
            try:
                response = table.scan()
            except ClientError as e:
                return respond(400,{"error": "There was an error loading the ToDo objects."})
            else:
                return respond(None, [response['Items']])
    
        elif event['requestContext']['resourcePath'] == "/v1/todo" and event['httpMethod'] == 'PUT':
            
            body = json.loads(event['body'])
            
            try:
                response = table.put_item(Item={'id': body['id'], 'title': body['title'], 'description': body['description']}, ConditionExpression='attribute_not_exists(id)') 
            except ClientError as e:
                return respond(400, {"error": "There was an error while updating the ToDo object."})
            else:
                return respond(None, {"message": "ToDo object updated successfully."})
                
        else:
            return respond(ValueError('Unsupported method.'))
            
    except:
        return respond(ValueError('Illegal arguments.'))
