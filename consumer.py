import json
from kafka import KafkaConsumer
from s3 import process_and_upload_image_to_s3
import dotenv
dotenv.load_dotenv()
import os

consumer = KafkaConsumer('image_topic',
                         bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))


def consume():
    for message in consumer:
        data = json.loads(message.value)
        encoded_image = data['image_data']
        metadata = data['metadata']

        process_and_upload_image_to_s3(encoded_image, filename=metadata['filename'])


if __name__ == '__main__':
    consume()
