import os
import time

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
    print(path)
    print(name)