import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler



if __name__ == "__main__":
    
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
