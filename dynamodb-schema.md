# Schema

- [Core Schema](#core-schema)
- [Resource Type: `DeliveryId`](#resource-type-deliveryid)
- [Resource Type: `SteeringMenu`](#resource-type-steeringmenu)
- [Resource Type: `Queue`](#resource-type-queue)

## Core Schema
| Attribute Name | Type | Description |
|----------------|------|-------------|
| Primary_Key | Primary Key | Unique Id of the Resource to be looked up |
| Resource_Type | Sort Key | The type of Resource (e.g. Queue, DeliveryId, Call Steering Menu Name) |


## Resource Type: `DeliveryId`
| Attribute Name | Type | Description |
|----------------|------|-------------|
| Queue_DeliveryId_DefaultQueue | String | The name of the Default Queue to be used |
| Flag_DeliveryId_NextActionType| String | Determines what the next part of the call should be, must be one of `queue, steeringmenu, flow, external, disconnect`|
| Flag_DeliveryId_NextActionValue| String | Value relating to the NextActionType, e.g. Queue Arn, Contact Steering Menu Name, Flow Arn, Phone Number, Message to play before disconnect|
| Prompt_DeliveryId_Welcome | String | The Welcome message to be played to the contact |
| Prompt_DeliveryId_WelcomeAdHoc | String | A ad-hoc message which can be updated on the fly without altering the welcome message |
<details>
    <summary>Example</summary>

```
{
    "Primary_Key": "+PHONE NUMBER",
    "Resource_Type": "DeliveryId",
    "Queue_DeliveryId_DefaultQueue": "QUEUE ARN",
    "Flag_DeliveryId_NextActionType": "steeringmenu",
    "Flag_DeliveryId_NextActionValue": "SampleDepartment_Retail",
    "Flag_DeliveryId_CustomerProfiles": "enabled",
    "Prompt_DeliveryId_Welcome": "Welcome to Sample Department.",
    "Prompt_DeliveryId_WelcomeAdHoc": ""
   }
```

</details>

## Resource Type: `SteeringMenu`
| Attribute Name | Type | Description |
|----------------|------|-------------|
| Prompt_SteeringMenu_PreMenuOptions | String | Message to be played before the contact is able to select an option |
| Prompt_SteeringMenu_MenuOptions | String | Message to be played which gives the contact the options they can select |
| Flag_SteeringMenu_Retries | String | Number of retries given to the customer |
| Prompt_SteeringMenu_Retry | String | Message to be played when the option selected was not recognised and the menu is to be played again |
| Flag_SteeringMenu_NextActionType_[0-9, Star, Hash, Default] | String | Determines what the next part of the call should be, must be one of `queue, steeringmenu, flow, disconnect`, where the last section of the attribute name describes which option was selected (*NOTE*: Every Steering Menu **MUST** contain a Default option) |
| Flag_SteeringMenu_NextActionValue_[0-9, Star, Hash, Default] | String | Value relating to the NextActionType, e.g. Queue Name, Contact Steering Menu Name, Flow Arn, Message to play before disconnect |
| Flag_SteeringMenu_NextActionPrompt_[0-9, Star, Hash, Default] | String | Prompted to be played after the selection is made, but before it goes to the NextAction |
| Flag_SteeringMenu_OutOfHourActionType | String | Determines what to do when out of hours, must be one of `queue, prompt, flow, disconnect` |
| Flag_SteeringMenu_OutOfHourValue | String | Value relating to the OutOfHourActionType, e.g. Queue Arn, Prompt Wording, Flow Arn, Message to play before disconnect |

<details>
    <summary>Example</summary>

```
{
    "Primary_Key": "SampleDepartment_Retail",
    "Resource_Type": "SteeringMenu",
    "Flag_SteeringMenu_NextActionType_1": "steeringmenu",
    "Flag_SteeringMenu_NextActionType_2": "steeringmenu",
    "Flag_SteeringMenu_NextActionType_3": "queue",
    "Flag_SteeringMenu_NextActionType_9": "steeringmenu",    
    "Flag_SteeringMenu_NextActionType_Default": "queue",
    "Flag_SteeringMenu_NextActionValue_1": "SampleDepartment_Retail_NewProduct",
    "Flag_SteeringMenu_NextActionValue_2": "SampleDepartment_Retail_ExistingProduct",
    "Flag_SteeringMenu_NextActionValue_3": "QUEUE ARN",
    "Flag_SteeringMenu_NextActionValue_9": "SampleDepartment_Retail",
    "Flag_SteeringMenu_NextActionValue_Default": "QUEUE ARN",
    "Flag_SteeringMenu_Retries": "1",
    "Prompt_SteeringMenu_MenuOptions": "For information on purchasing a new product, please press 1. For information on a product you have already purchased, press 2. For anything else, please press 3. To repeat these options, press 9.",
    "Prompt_SteeringMenu_PreMenuOptions": "I will now give you 3 options",
    "Prompt_SteeringMenu_Retry": "Sorry, we didnt detect a valid entry."
}
```

</details>


## Resource Type: `Queue`
| Attribute Name | Type | Description |
|----------------|------|-------------|
| Flag_Queue_ContactRecording | String | `enabled \| disabled` (Default enabled) |
| Flag_Queue_ScreenRecording | String | `enabled \| disabled` (Default disabled) |
| Flag_Queue_Analytics | String | `postcall \| realtime \| disabled` (Default disabled) |
| Flag_Queue_Redaction | String | `RedactedAndOriginal \| Redacted` (Default RedactedAndOriginal) |
| Prompt_Queue_WhisperAgent | String | Prompted to be played to the Agent as the call is connected |
| Prompt_Queue_WhisperCustomer | String | Prompted to be played to the Customer as the call is connected |
| Flag_Queue_OutOfHourActionType | String | Determines what to do when out of hours, must be one of `queue, steeringmenu, flow, disconnect` |
| Flag_Queue_OutOfHourActionValue | String | Value relating to the OutOfHourActionType, e.g. Queue Arn, Contact Steering Menu Name, Flow Arn, Message to play before disconnect |

<details>
    <summary>Example</summary>

```
{
    "Primary_Key": "SampleDepartment_Default",
    "Resource_Type": "Queue",
    "Flag_Queue_Analytics": "realtime",
    "Flag_Queue_ContactRecording": "enabled",
    "Flag_Queue_OutOfHourActionType": "disconnect",
    "Flag_Queue_OutOfHourActionValue": "Sorry, we are currently closed",
    "Flag_Queue_Redaction": "RedactedAndOriginal",
    "Flag_Queue_ScreenRecording": "enabled",
    "Prompt_Queue_WhisperAgent": "Sample Department - Default",
    "Prompt_Queue_WhisperCustomer": "Now connecting you with $.Agent.FirstName",
    "Prompt_Queue_PreQueue": "All calls are monitored or recorded for quality and training purposes."
   }
```