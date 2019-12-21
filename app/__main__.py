import webbrowser
import os
import threading
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Add browser support.')
parser.add_argument('-b', help="Specify which browswer to launch the editor in: either chrome or firefox")

args = parser.parse_args()

path = ''
if args.b == 'chrome': 
    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
elif args.b == 'firefox': 
    path = 'C:\Program Files\Mozilla Firefox\Firefox.exe'


#Check for dependencies
with open('requirements.txt') as requirements:
    result = subprocess.check_output('pip freeze', shell=True)
    result = str(result)
    reqs = requirements.read().splitlines()
    for req in reqs:
        if req+'==' not in result:
            os.system(f'pip install {req}')



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