from bs4 import BeautifulSoup
import requests


def get_post_link(categories, page):
    """Get post link and initial entries link list"""

    link = str(categories) + str(page)  # add link with page number
    html_content = requests.get(link).text  # get html content in text format
    soup = BeautifulSoup(html_content, 'html.parser')  # parse html text content to bs4 object

    links_with_text = []  # initial list of post links

    # get all <a> tag with <href not null> and text equal "Xem thêm"
    for h in soup.findAll('a', href=True, text="Xem thêm"):
        if h.text:
            links_with_text.append(h['href'])
    return links_with_text
