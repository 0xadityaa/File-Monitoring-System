import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import getpass


if __name__ == "__main__":
    # Setting a format for logger
    user = getpass.getuser()
    logging.basicConfig(filename="watcher.log",
        filemode='a',
        level=logging.INFO,
        format="%(asctime)s - %(process)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    # Give path to the target file or directory.
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print("🎯 Target Set to: " + path)

    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
