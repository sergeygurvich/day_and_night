from kafka import KafkaProducer
import json

from utils import encodeb64

producer = KafkaProducer(bootstrap_servers='192.168.0.27:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def produce(message):
    producer.send('image_topic', value=message)
    producer.flush()


def create_message_with_metadata(file_path, metadata):
    # Base64 encode the image
    encoded_image = encodeb64(file_path)

    # Create a dictionary for the message
    message = {
        "image_data": encoded_image,
        "metadata": metadata
    }

    # Convert the dictionary to a JSON string
    return json.dumps(message)
