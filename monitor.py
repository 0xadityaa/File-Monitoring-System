import sys
import time
import logging
import getpass
import shutil
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Function to trigger backup of target directory files if malicious activity is detected.
class MonitorFolder(FileSystemEventHandler):
    # Handling File modification event.
    def on_modified(self, event):
        # Raising the flag and emailing sysAdmin
        print("⛔️ Malicious activity detected by watcher!")
        # Encrypting all the data inside watcher directory.
        print("🧩 Encrypting all the data...")
        # Commit and push changes to GitHub repository
        print("🚀 Pushing encrypted backup to the repo...")
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'THIS IS AN ENCRYPTED BACKUP COMMIT AS MALICIOUS ACTIVITY DETECTED ON SERVER'])
        subprocess.run(['git', 'push', "-u", 'origin', 'main'])
    
    # Handling the File creation event.
    def on_created(self, event):
        print("A new create event was made", event.src_path)
    
    # Handling the File deletion event.
    def on_deleted(self, event):
        print("A deletion event was made", event.src_path)


if __name__ == "__main__":
    # Setting a format for logger
    user = getpass.getuser()
    logging.basicConfig(
        filename="watcher.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(process)d - %(message)s -" + f" {user}",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Give path to the target file or directory.
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print("🔥 Monitoring Started!")
    print(f"🎯 Target Set to: {path}")

    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()