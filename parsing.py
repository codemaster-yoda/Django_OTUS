#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import re
import sys

mr_ninja = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣤⡀\n⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣄⣶⣿⠟⠛⠉⠀⠀⠀⢀⣹⣿⡇\n⠀⠀⠀⠀⢀⣤⣾⣿⡟⠛⠛⠛⠉⠀⠀⠀⠀⠒⠒⠛⠿⠿⠿⠶⣿⣷⣢⣄⡀\n⠀⠀⠀⢠⣿⡟⠉⠈⣻⣦⠀⠀⣠⡴⠶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣮⣦\n⠀⠀⢰⣿⠿⣿⡶⠾⢻⡿⠀⠠⣿⣄⣠⣼⣿⡇⠀⠈⠒⢶⣤⣤⣤⣤⣤⣴⣾⡿\n⠀⠀⣾⣿⠀⠉⠛⠒⠋⠀⠀⠀⠻⢿⣉⣠⠟⠀⠀⠀⠀⠀⠉⠻⣿⣋⠙⠉⠁\n⠀⠀⣿⡿⠷⠲⢶⣄⠀⠀⠀⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣦\n⠛⠛⢿⣅⣀⣀⣀⣿⠶⠶⠶⢤⣾⠋⠀⠀⠙⣷⣄⣀⣀⣀⣀⡀⠀⠘⣿⣆\n⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠈⠛⠛⠶⠾⠋⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠛
"""


URL = 'https://yummyanime.tv/series-y1/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

new_urls = set()
def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:

            return response.text
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        sys.exit('Error:status_code != 200')

def parse_HTML(html_document):
    all_links = []
    soup = bs(html_document, 'html.parser')
    for link in soup.find_all('a', attrs={'href': re.compile('^https://')}):
        all_links.append(link.get('href'))
    return all_links
new_urls.update(parse_HTML(get_html(URL)))

final_all_links = []
for i in new_urls:
    final_all_links.append(parse_HTML(get_html(i)))
_input = input("Press P or F :").upper()
if _input == 'P':
    print(mr_ninja, final_all_links)

elif _input == 'F':
    file_name = input('Enter file name: ')
    with open(f'{file_name}', 'w') as f:
        f.writelines(str(final_all_links))
        f.close()
else:
    sys.exit('\n' + mr_ninja + '\nmessage:input invalid')
