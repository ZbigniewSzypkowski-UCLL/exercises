import requests
import re

def extract_urls(url):
    response = requests.get(url)
    html_content = response.text

    url_pattern = r"https?://[^\s]+?\.(?:jpg|jpeg|png|svg|gif|ico)"
    urls = re.findall(url_pattern, html_content)
    return urls
    """
    eindigd met .png
    """

def main():
    url = "https://www.ucll.be/nl"
    urls = extract_urls(url)
    print("Extracted URLs: ")
    for url in urls:
        print(url)

main()