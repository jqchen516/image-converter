import configparser
import os
import sys

from PIL import Image
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

SOURCE_PATH = "C:\\wid120\\"
DESTINATION_PATH = "C:\\packer\\waferid.jpg"
image_extensions = {'.jpg', '.jpeg'}


class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            _, ext = os.path.splitext(event.src_path)
            if ext.lower() in image_extensions:
                print("===================================")
                print(f"new image detected: {event.src_path}")
                im = Image.open(event.src_path)
                im = im.convert("RGB")
                im.save(DESTINATION_PATH)
                print(f"save new image to {DESTINATION_PATH}")
                print("===================================")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(sys.executable))
    config_path = os.path.join(base_path, 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)
    SOURCE_PATH = config['path']['source']
    DESTINATION_PATH = f"{config['path']['destination']}{config['path']['file']}"
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=SOURCE_PATH, recursive=False)
    observer.start()
    print(f"Start listen path: {SOURCE_PATH}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        print("Stop listen")
    observer.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
