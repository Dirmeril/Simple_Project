import os
import csv
from flask import Flask

app = Flask(__name__)


def append_csv_data(data):
    full_file_path = os.path.join(app.static_folder, 'trips.txt') 
    fieldnames = ['trip_text', 'email', 'short_text', 'completness', 'contact', 'id']
    
    if not os.path.exists(full_file_path):
        with open(full_file_path, 'w+', newline='',encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    with open(full_file_path, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)


def read_csv_data():
    full_file_path = os.path.join(app.static_folder, 'trips.txt')
    fieldnames = ['trip_text', 'email', 'short_text', 'completness', 'contact', 'id']

    entries = []
    with open(full_file_path, mode='r', encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        line_count = 0 
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
            else:
                entries.append(row)
                line_count += 1
    return entries
