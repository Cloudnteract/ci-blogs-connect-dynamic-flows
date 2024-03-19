import logging
import os
import boto3

LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
DDB_TABLENAME = os.environ.get("DDB_TABLENAME", "NOTFOUND")

root_logger = logging.getLogger()
root_logger.setLevel(logging.WARN)
log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)
log.info(f"Lambda Initiated, LOG_LEVEL = {LOG_LEVEL}, DDB_TABLENAME = {DDB_TABLENAME}")

resource_ddb = boto3.resource('dynamodb')
ddb_table = resource_ddb.Table(DDB_TABLENAME)
log.debug(f"DynamoDb Resource Created for table: {DDB_TABLENAME}")

def get_ddb_item(primary_key, resource_type):
    response_ddb = ddb_table.get_item(
        Key={
            'Primary_Key': primary_key,
            'Resource_Type': resource_type
            }
        )
    log.debug(f"DynamoDb GetItem Response: {response_ddb}")

    if 'Item' in response_ddb:
        log.debug(f"Item Found: {response_ddb['Item']}")
        response = response_ddb['Item']
    else:
        log.error(f"No Item Found for Primary Key: {primary_key}, Resource Type: {resource_type}")
        response = None
    return response


def lambda_handler(event, context):
    log.debug(f"Event: {event}")
    log.debug(f"Context: {context}")
    primary_key = event.get("Details", {}).get("Parameters", {}).get("Primary_Key")
    resource_type = event.get("Details", {}).get("Parameters", {}).get("Resource_Type")
    
    if primary_key is not None and resource_type is not None:
        log.info(f"Fetching Config for Primary_Key: {primary_key}, Resource_Type: {resource_type}")
        response = get_ddb_item(primary_key, resource_type)
    else:
        # At least one of 'Primary_Key' or 'Resource_Type' is missing or has a None value
        log.error("One or both of 'Primary_Key' and 'Resource_Type' are missing or have a None value.")
        response = None

    log.info(f"Returning: {response}")
    return response