"""Scope of this script is to grab date from a site,
clean the garbage and store need data to a dictionary"""
import re
import requests
from bs4 import BeautifulSoup

response = requests.get("https://whatweekisit.com")
soup = BeautifulSoup(response.content, "html.parser").table
out = list(soup.find_all('tr'))
out_len = len(out)
d_date = {}


def remove_html_tags(text):
    """Pas a text as argument, remove html tags and return the result"""
    text = str(text)
    new_text = re.sub('<[^<]+?>', '', text)
    return new_text


for x in range(0, out_len):
    ARG1 = str(x)
    ARG2 = remove_html_tags(out[x])
    DELIMITER = ':'
    if DELIMITER in ARG2:
        # print("Position: {} contains: {}".format(ARG1, ARG2))
        xxx = ARG2.split(DELIMITER)
        d_date[xxx[0]] = xxx[1]

print("Some information about today:\n"
      "INFO: Data collected from: https://whatweekisit.com\n"
      "===================================================")
for key in d_date:
    print("{}: {}".format(key, d_date[key]))
