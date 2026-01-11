import requests
from pathlib import Path

URL = 'https://adventofcode.com/{}/day/{}/input'

token = None
session_file = Path('session.txt')
if not session_file.is_file():
    print('Lets create a file to store your AoC session token')
    token = input('AoC session token: ')
    with open(session_file, 'w') as f:
        f.write(token)
        print('Session token saved as', f.name)
else:
    token = session_file.read_text()

year = input('year: ')
day = input('day: ')

response = requests.get(URL.format(year, day), cookies={'session': token})
if response.status_code < 200 or response.status_code >= 300:
    print('Downloading input failed')
else:
    with open(f'{year}_{day}.in', 'w') as f:
        f.write(response.text)
        print('Input saved as', f.name)
