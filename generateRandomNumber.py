import json
import random
import boto3




def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('randomNumber')
    
    num = random.randrange(int(event['start']), int(event['stop']))
    sum_of_numbers = int(event['start']) + int(event['stop'])
    
    response = table.put_item(
        Item={
        "number": str(num),
        'sum': sum_of_numbers
        })
    alert_body = "Your random number between "+str(event['start'])+" and "+str(event['stop'])+" is: "+str(num)+", and their sum is: "+ str(sum_of_numbers)
    
    return {
        'statusCode': 200,
        'your_first_num': json.dumps(str(event['start'])),
        'your_second_num': json.dumps(str(event['stop'])),
        'random_number': json.dumps('Your random number between is: ' + str(num)),
        'sum_of_numbers': json.dumps('Sum of your numbers is: ' 
        + str(sum_of_numbers)),
        "body": alert_body
    }
