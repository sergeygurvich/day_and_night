from camera import capture
from producer import produce, create_message_with_metadata
import time

if __name__ == '__main__':

    number_of_pics = 10
    i = 0
    # while i < number_of_pics:
    while True:
        file_path, filename = capture(0)

        if file_path:
            metadata = {
                'filename': filename
            }
            message = create_message_with_metadata(file_path, metadata)
            produce(message)

        time.sleep(60*10)
        i += 1
