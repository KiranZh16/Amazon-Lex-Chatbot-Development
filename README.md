**Amazon Lex Chatbot Development: Banker’s Bot**

This document outlines the complete, step-by-step process followed to create a Banker’s Bot using Amazon Lex, including intents, slot configuration, Lambda integration, and context handling. The goal of this bot is to enable users to check account balances, transfer funds, and make payments. While alternative methods may exist, the flow below reflects the exact implementation steps taken during development.

**1. Bot Creation**

-Created a new Amazon Lex bot from scratch.

-Bot Name: BankersBot

-Description: Banker’s Bot can check the balance, transfer funds, and make a payment.

![image](https://github.com/user-attachments/assets/ebafd623-1c3b-4e02-b8f8-53d558963e6f)


**2. IAM Permissions**

-Created a role with basic Amazon Lex permissions


**3. Bot Voice Selection**

-Chose a suitable Amazon Polly voice for bot responses.

**4. Welcome Intent**

-Created WelcomeIntent with a friendly welcome message.

-Example utterance: "Hi, how can I help you today?"

-Tested the bot to ensure the welcome message was triggered.

![image](https://github.com/user-attachments/assets/bec2e4c1-4517-4c6f-8a88-070241731072)

![image](https://github.com/user-attachments/assets/806e4c7c-6d5e-443d-9bea-c0a9d013f652)


**5. Fallback Intent**

-Configured FallbackIntent to handle unrecognized input.

-Added multiple utterance variations to increase coverage.

-Re-tested the bot to verify fallback behavior.

![image](https://github.com/user-attachments/assets/32982e43-892e-46ed-8b57-254925d394c3)

![image](https://github.com/user-attachments/assets/4ad2e3fd-50ad-45a4-a579-8f6edf6fa779)

![image](https://github.com/user-attachments/assets/89f88a0f-5535-495b-80a5-c41f2e51fed7)




**6. Slot Types and Account Balance Check**

-Created a custom slot type AccountType with values:

 Chequing

 Savings

 Credit Card

![image](https://github.com/user-attachments/assets/77a7f3e3-ce68-49b4-999b-76f60a77e871)


**Created intent: CheckBalance**

-Added slots:

-AccountType

-DateOfBirth

-Bot prompt: "Which account would you like your balance for?"

-Tested the bot to verify slot prompting and intent triggering.

![image](https://github.com/user-attachments/assets/6739b2b0-117c-47ee-9a70-1b97d2c82a59)

![image](https://github.com/user-attachments/assets/69df1901-6c0c-4155-a43c-21094e4f8cd3)



**7. Lambda Function: Simulated Balance Generator**

-To simulate real bank balance data, a Lambda function was implemented to return a random balance response. The function was connected to the CheckBalance intent.

-Function Purpose:

-Extracts AccountType and DateOfBirth from user input.

-Validates both slots are provided.

-Generates a random balance between $100 and $10,000.

-Returns a formatted message including account type and date of birth.

-Test Result:

-Example response:

"Your savings account balance is $3,417.85. Thanks for verifying your date of birth: 1992-07-15."

* Lambda code is provided in code
 
**8. Lex Alias and Lambda Connection**

-Created a Lex alias.

-Enabled code hook in fulfillment section of the intent.

-Connected the above Lambda function.

-Rebuilt the bot.

![image](https://github.com/user-attachments/assets/acbdb128-31e3-40f6-b340-f61f1af0e113)

![image](https://github.com/user-attachments/assets/3b78f24d-121d-428b-81b1-aa2af8e2135c)

![image](https://github.com/user-attachments/assets/26a08ae3-e3f2-4028-9b28-388181e1a9fd)


**9. Context Handling**

-Added output context contextCheckBalance in CheckAccountBalance intent.

![image](https://github.com/user-attachments/assets/52a587e3-fec1-41d4-ac70-053478897c2f)


-Created follow-up intent FollowupCheckBalance

-Description: Allow follow-up balance check without re-authentication.

-Input context: contextCheckBalance

![image](https://github.com/user-attachments/assets/9f634409-46cd-44f7-a951-3f14241b58fc)

-Added utterances like:

"Check my savings again"

"What's the balance in my chequing?"

-Added slots AccountType and DateOfBirth

![image](https://github.com/user-attachments/assets/df2110ec-e7f7-4b36-bd68-94b1b81444cb)


-Reused previous value of DateOfBirth using #contextCheckBalance.dateOfBirth

![image](https://github.com/user-attachments/assets/a36dce90-89df-45fe-9262-bfc6217327c4)


-Connected Lambda for fulfillment.

**Rebuilt and tested bot: it remembered previous date of birth.**


-**10. Transfer Funds Intent**

-Created intent: TransferFunds

-Description: Helps users transfer funds from one account to another.

![image](https://github.com/user-attachments/assets/da9af785-a506-4e87-bdcc-b55a9c9918e5)


-Defined utterances:

"Transfer $100 from savings to chequing"

-Defined slots:

SourceAccountType

TargetAccountType

TransferAmount

![image](https://github.com/user-attachments/assets/1d71cf4e-2c6f-4d0d-898d-680597a89a95)


-Set up confirmation prompt

![image](https://github.com/user-attachments/assets/a2477ff7-800a-4421-a3c1-b3a917fb6e69)


-Built and tested successfully.

![image](https://github.com/user-attachments/assets/052be083-9a55-4aff-8b9f-834a615048e3)

![image](https://github.com/user-attachments/assets/f1d4956c-a7c6-4a11-a456-0751e0bd52be)


Conclusion

The Banker’s Bot demonstrates how Amazon Lex can be used to build intelligent, voice/text-based financial services. It includes context management, slot reuse, Lambda integration, and user-friendly prompts. Future improvements could include authentication layers, integration with banking APIs, and enhanced slot validation.

