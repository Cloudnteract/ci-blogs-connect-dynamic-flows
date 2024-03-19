# Amazon Connect - Flow Configuration
Stores configuration to be used by Flows in order to provide a dynamic customer journey.

## Features

* Based on Dialled Number:
    * Welcome Prompt
    * Ad-Hoc Welcome Prompt
    * Various destinations:
        * Steering Menu
        * Defined Contact Flow
        * Queue
        * External Number
        * Disconnect
* Based on Queue
    * Call Recording
    * Analytics
    * Redaction
    * Screen Recording
    * Agent/Customer Whisper
    * Various Out of Hours destinations
* Data driven Call Steering Menus:
    * Pre Menu Prompt (non-interruptable)
    * Menu Prompt (interruptable)
    * Retries (upto 3)
    * Retry Prompt
    * Selectable Options 0-9
    * Default Option (Retries exceeded)
    * Various destinations:
        * Another Steering Menu
        * Defined Contact Flow
        * Queue
        * External Number
        * Disconnect


## Pre-Reqs

* An AWS account with access to the services mentioned 
* An Amazon Connect instance, configured and taking inbound/making outbound calls 

## Deployment

1. Create a new CloudFormation Stack using the template `.\src\cloudformation\cfn-connect-dynamic-flow-data.yaml`, this will deploy the following resources:
    * DynamoDb Table for Contact Flow Data to be stored
    * Lambda used by the Contact Flow to retrieve data to be used
    * Core set of Contact Flow Modules/Contact Flows
    * Some example Queues and Hours of Operation to be used as part of this guide (can be omitted if you wish to use your own resources)
1. Create a DynamoDb Item for each JSON file: (Table Name can be found in Stack Outputs: oDynamoDbTableConnectFlowDataName)
    * `.\src\dynamodb\DeliveryId\`: Updating the Primary_Key to the Delivery Phone number claimed in your Connect Instance (in e.164 format)
    * `.\src\dynamodb\Queue\`: Updating the Primary_Key to the Queue Name (each Queue should have its own item in DynamoDb)
    * `.\src\dynamodb\SteeringMenu\`: Updating any destinations that require a ARN (e.g. Queue/Contact Flow ARN's)

## Documentation
| Item | Description |
|------|-------------|
| [DynamoDb Schema](./dynamodb-schema.md) | Explaination behind the DynamoDb table structure and how to use it |
