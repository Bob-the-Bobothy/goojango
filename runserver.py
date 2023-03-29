import os
import subprocess
import sys

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class ReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Reload the server whenever a file changes
        subprocess.run(["touch", "reload.txt"])

def start_server():
    # Start the Django server in a separate process
    subprocess.Popen("python manage.py runserver")

if __name__ == "__main__":
    # Start the server
    start_server()

    # Watch for file changes
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        # Keep the main thread running until KeyboardInterrupt
        while True:
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()