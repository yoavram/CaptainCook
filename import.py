import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from common import *
from models import *
from os.path import basename

class Importer(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            logging.warn("No support for folder importing!")
            return
        if event.event_type != 'created':
            raise Exception("Expected a creation event.")
        
        path = basename(event.src_path)
        try:
            Recipe.get(Recipe.image==path)
        except DoesNotExist:
            recipe = Recipe.create(name='', image=path)
            logging.info("New recipe in file %s", path)


if __name__ == "__main__":
    event_handler = Importer()
    observer = Observer()
    observer.schedule(event_handler, path='import', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()