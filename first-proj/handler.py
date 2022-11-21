import json


def hello(event, context):
    json.dumps(event)
    print(event)
    print(type(event))
    json.loads(event)
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    return {"statusCode": 200, "body": json.dumps(body)}

def inputval(event, context):
    # if val == 0:
    #     res = 0
    # elif val == 1:
    #     res = 1
    # else:
    #     res = f"{val} is graterthan one"
    return {"statusCode": 200, "body": json.dumps('res')}
