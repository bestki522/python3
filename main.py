from bs4 import BeautifulSoup
import requests
import get_post_link

# initial result in list object
my_post_link = []

# run function with 1st, 2nd page
for p in range(1, 3):
    temp_link = get_post_link.get_post_link("https://chiasemoi.com/tai-sach/sach-nuoi-day-con/page/", p)
    my_post_link.extend(temp_link)

print(my_post_link)
