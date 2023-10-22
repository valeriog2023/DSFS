#! /usr/bin/env python
#
# beaautiful soup creates a tree from a webpage and provides a way to navigate it
# this requriees the library to be installed
# pip install beautifulsoup4,html5lib,requests
#
# This script uses the html page at this url:
# https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html
# a copy of the page is in data_files
from bs4 import BeautifulSoup
import requests

url = "https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html"
# Note you an also define it as:
# url = ( "https://raw.githubusercontent.com/",
#         "joelgrus/data/master/getting-data.html")
# and they will get concatenated
print(f"--- Getting page: {url}")
r = requests.get(url)
html = r.text
#
# now let's build the object
# the html5lib is the engine used to parse the page
soup = BeautifulSoup(html,'html5lib')
#
print("\nWe need to work with Tag objects that make the structure of the HTML page")
#
# find the first paragraph <p>; this is an object
first_paragraph = soup.find('p')     # same as soup.p
#
# you can now check what it's inside
print(f"Text inside the 1st paragraph: {first_paragraph.text}")
print(f"Paragaph attributes soup.p.attrs: {soup.p.attrs}")
print(f"Paragaph id: soup.p.get('id'): {soup.p.get('id')}")
print("--------")
print("Find all paragraphs and their texts")
all_p = soup.find_all('p')
all_p_ids_and_texts = [(p.get('id'),p.text) for p in all_p]
for id,t in all_p_ids_and_texts:
    print(f"p:{str(id):>4}, text: {t}")
#
# to find tags with a specific class you can specify it
important_p1 = soup.find_all('p',{'class':'important'})
important_p2 = soup('p',{'class':'important'})
important_p3 = soup('p','important')
important_p4 = [ p for p in soup('p') if 'important' in p.get('class',[]) ]
print("-----------")
print("Filter paragraphs based on attribute class as example (4 different methods)")
print(important_p1)
print(important_p2)
print(important_p3)
print(important_p4)


#
# running the same with the local file     
print("\n---------\nNow reading local file.. extra span added there..")
with open("data_files/getting-data.html") as f:
    text = f.read()
soup =  BeautifulSoup(text,'html5lib')
#
# some "complex" search
# returns all 'spans' coming from all divs
print("-----------")
print("Some more complex parsing to return al spans inside all divs")
spans_inside_divs = [(span, div) 
                     for div in soup.findAll('div')
                     for span in div('span') ]
for span,div in spans_inside_divs:
    print(f"span: {span} \nfrom div:\n    {div}\n--")
    

