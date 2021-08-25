import http.client
import logging
import os
import json
from urllib import request, parse, error
import base64
import azure.functions as func
from azure.storage.blob import BlobClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def main(event: func.EventHubEvent):

    # Metadata
    for key in event.metadata:
        logging.info(f'Metadata: {key} = {event.metadata[key]}')

    message_body = event.get_body().decode()
    message_body_json = json.loads(message_body)

    key = "165be6bc0ac0444b81ab0bf3bc121af5"
    endpoint = "https://textlangdetection.cognitiveservices.azure.com/"

    def authenticate_client():
        ta_credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
        return text_analytics_client

    client = authenticate_client()

    def key_phrase_extraction_example(client):
        try:
            message_list = []
            message_list[0] = message_body_json['body']
            documents = message_list
            response = client.extract_key_phrases(documents=documents)[0]
            if not response.is_error:
                logging.info(f'key phrases - {response.key_phrases}')
                return ','.join(str(x) for x in response.key_phrases)
            else:
                return str(response.error)
        except Exception as err:
            print("Encountered exception. {}".format(err))

    key_words = key_phrase_extraction_example(client)
    message_body_json["key_words"] = str(key_words)

    blobContent = {
        "enqueuedAt": f'{event.enqueued_time}',
        "partitionId": event.metadata['PartitionContext']['PartitionId'],
        "eventContent": json.dumps(message_body_json)
    }
    blobName = f'{blobContent["partitionId"]}/{event.enqueued_time.year}/{event.enqueued_time.month}/{event.enqueued_time.day}/{event.enqueued_time.hour}_{event.sequence_number}_{event.offset}_{"key-words"}'

    sa_cs = "DefaultEndpointsProtocol=https;AccountName=dmytraha3uaydsa;AccountKey=iiNDg21mS5Ng+AbDmJLFvqG7OfKv+vIQfVd4xm0qP7T58vRHayo153rld4fzwgRn+DYTHOo9LhDRq44jm8rvSA==;EndpointSuffix=core.windows.net"
    sa_container = "events"
    blob = BlobClient.from_connection_string(conn_str=sa_cs, container_name=sa_container, blob_name=blobName)

    blob.upload_blob(json.dumps(blobContent))
