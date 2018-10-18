# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "http://bindeleddet.no/events/1954/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Google" occurs on the page is less than 1,
    # print(str(soup).find("Ikke aktuell"))

    print(soup)

    # wait 60 seconds,

    time.sleep(5)
    # continue with the script,
    continue
