import webbrowser
import os
import threading

import argparse

parser = argparse.ArgumentParser(description='Add browser support.')
parser.add_argument('-b')

args = parser.parse_args()

path = ''
if args.b == 'chrome': 
    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
elif args.b == 'firefox': 
    path = 'C:\Program Files\Mozilla Firefox\Firefox.exe'

def main_thread():
    other = threading.Thread(target=flask_thread, args=())
    other.start()
    try:
        webbrowser.get(path).open('http://127.0.0.1:5000')
    except:
        webbrowser.open('http://127.0.0.1:5000')
def flask_thread():
    os.system("flask run")

main_thread()