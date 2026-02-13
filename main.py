import os
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


SOURCE_PATH = "C:\\wid120\\"
SOURCE_PATH = "imageSource/"
DESTINATION_PATH = "C:\\packer\\waferid.jpg"
DESTINATION_PATH = "imageDestination/b.jpg"
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
