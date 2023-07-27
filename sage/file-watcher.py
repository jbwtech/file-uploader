import os
import time
import hashlib
import subprocess

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def get_file_list(directory): 
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def wait_new_files(directory): 
    previous_files = get_file_list(directory)
    while True:
        current_files = get_file_list(directory)
        new_files = list(set(current_files) - set(previous_files))
        for new_file in new_files:
            print("New file created:", new_file)
            file_path = os.path.join(directory, new_file)
            file_name = os.path.basename(file_path)
            upload_file(file_path, file_name)
        previous_files = current_files
        time.sleep(1)

def upload_file(path, name):
    print("PATH  : ", path)
    print("FILE  : ", name)
    sum = sha1sum(path)
    print("SHA1  : ", sum)
    sum = sha256sum(path)
    print("SHA256: ", sum)
    texfile = path
    subprocess.run(['pdflatex', '-interaction=nonstopmode', texfile])

    pdfl = PDFLaTeX.from_texfile(texfile)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

def sha1sum2(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha1').hexdigest()

def sha1sum(filename):
    h  = hashlib.sha1()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    file_path = event.src_path
    file_name = os.path.basename(file_path)
    upload_file(file_path, file_name)

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = "/files/uploads"
    go_recursively = True

    print("Running file-watcher ... ")
    
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()

    try:
        while True:
            time.sleep(1)
            # wait_new_files(path)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
        exit