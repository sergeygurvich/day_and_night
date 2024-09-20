import base64

def encodeb64(file_path):

    with open(file_path, "rb") as image_file:
        image_bytes = image_file.read()

    # Encode the binary data to Base64
    encoded_image = base64.b64encode(image_bytes)

    # Convert Base64 bytes to string
    base64_string = encoded_image.decode('utf-8')

    # Print or use the Base64 string
    return base64_string


def decodeb64(base64_string):
    # Decode the Base64 string into bytes
    image_data = base64.b64decode(base64_string)

    return image_data