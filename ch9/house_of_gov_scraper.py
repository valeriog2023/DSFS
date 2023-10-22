#! /usr/bin/env python
#
from bs4 import BeautifulSoup
import requests
import regex as re
import timeit
from typing import Dict,Set 
# scraping link: https://www.house.gov/representatives
# to get the list of representatives
url = "https://www.house.gov/representatives"

print(f"Getting page from: {url}")
text = requests.get(url).text
soup = BeautifulSoup(text,"html5lib")

#
# urls are in the form
# <a href="https://carl.house.gov">Carl, Jerry</a>
# where a is the tag
# and href is an attribute
all_urls = [ a['href'] for a in soup.find_all('a') if a.has_attr('href') ]

print(f"List of all anchors found has {len(all_urls)} elements")
print("some of these are references to local files or telephone numbers..")
print("e.g.\ntel:+12022243121\n/feature-stories")
print("some are not links for people.. which are in the format <name>.house.gov or <name>.house.gov/")
print("\nfilter out invalid urls..")
http_urls = [ u for u in all_urls if u.startswith("http") and
                                     (u.endswith("house.gov") or u.endswith("house.gov/"))
             ]
def conditional_match():
    _ = [ u for u in all_urls if u.startswith("http") and
                                (u.endswith("house.gov") or u.endswith("house.gov/"))
             ]

result = timeit.timeit(stmt='conditional_match', globals=globals(), number=5)
print(f"conditional match execution time result: {result}")
#
# note this can also be done via regex
# starts with http or https
# ends with .house.gov or house.gov/
pattern =  r"^https?:\/\/.*\.house\.gov/?$"
assert re.match(pattern, "http://joel.house.gov")
assert re.match(pattern, "https://joel.house.gov")
assert re.match(pattern, "http://joel.house.gov/")
assert re.match(pattern, "https://joel.house.gov/")
assert not re.match(pattern, "file://joel.house.gov/")
assert not re.match(pattern, "/joel")
assert not re.match(pattern, "https://joel.house.gov/path")

re_pattern_match_list = [ u for u in all_urls if re.match(pattern,u) ]
def regex_match():
    _ = [ u for u in all_urls if re.match(pattern,u) ]
result = timeit.timeit(stmt='regex_match', globals=globals(), number=5)
print(f"regex match execution time result: {result}")

assert re_pattern_match_list == http_urls
print("regex and conditional list matching are the same")
print(f"List of all anchors found has {len(http_urls)} elements")
print("----")
print("List has probably duplicates.. so let's create a set and then a list again")
unique_urls_list = list(set())
unique_urls_list = list(set(http_urls))
print(f"List of all anchors found has {len(unique_urls_list)} elements")
#
#
# Now we want to check every link to see if there are links to press-release
# also let's init a dict structure where the key is the website and the value is the set 
# of press release links
press_releases: Dict[str, Set[str]] = {}


def paragraph_mentions(html_text: str, keyword: str) -> bool:
    """This method accepts:
        html_text: text in html format
        keyword: string 
        returns true if the keyword is present in a tag <p> of html_text
    """
    soup = BeautifulSoup(html_text,'html5lib')
    #
    # it seems that p.get('text') returns empty and it is differente from p.text    
    return any([keyword.lower() in p.text.lower() for p in soup.find_all('p') ] )

text = """<body><h1>Facebook</h1><p>Twitter</p></body>"""
assert paragraph_mentions(text,'twitter')
assert not paragraph_mentions(text,'facebook')

print("\n------------\nNow let's check press release links in the representative websites")

for url in unique_urls_list:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'html5lib')
    press_links = {a['href'] for a in soup.find_all('a') if 'press release' in a.text.lower()}
    if press_links != {}:
        print(f"Representative site: {url} - press release {press_links}")
        press_releases[url] = press_links

#
print("We look for press release that concern data.. so we parse them all and filter filter based on that")
print("we basically want to know who is interested in data")
for house_url, pr_links in press_releases.items():
    for pr_link in pr_links:
        full_url = f"{house_url}/{pr_link}"
        html_text = requests.get(url).text

        if paragraph_mentions(html_text, 'data'):
            print(f"{house_url}")
            break # we jus wan to know who is interested


