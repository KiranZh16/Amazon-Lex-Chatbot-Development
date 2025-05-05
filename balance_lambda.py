import json
import random

def lambda_handler(event, context):
    intent_name = event['sessionState']['intent']['name']
    
    if intent_name == "CheckBalance":
        slots = event['sessionState']['intent']['slots']
        
        account_type = slots.get('AccountType', {}).get('value', {}).get('interpretedValue')
        dob = slots.get('DateOfBirth', {}).get('value', {}).get('interpretedValue')
        
        if not account_type or not dob:
            return {
                "sessionState": {
                    "dialogAction": {"type": "Close"},
                    "intent": {"name": intent_name, "state": "Failed"}
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "I'm missing some information. Please provide your account type and date of birth."
                    }
                ]
            }

        balance = round(random.uniform(100, 10000), 2)
        message = f"Your {account_type} account balance is ${balance:,.2f}. Thanks for verifying your date of birth: {dob}."

        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {"name": intent_name, "state": "Fulfilled"}
            },
            "messages": [
                {"contentType": "PlainText", "content": message}
            ]
        }

    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": intent_name, "state": "Fulfilled"}
        },
        "messages": [
            {"contentType": "PlainText", "content": "Sorry, I couldn't process your request."}
        ]
    }
