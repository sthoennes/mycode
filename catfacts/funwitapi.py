#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
#import random
import shutil
import urllib.request

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

    #print(r.url)
    #print()
    #print(r.text)
    #print(r.status_code)
    #print(r.iter_lines)
    #print("")
    #print(r.raw)
    list=print(r.json())
    print(type(list))
    buildlist = []
    #for catfact in r.json():
     #   buildlist.append(catfact.get("text"))
        #print(catfact.get("text"))  # the .get() method returns NONE if key not found
        #print(type(catfact.get("text")))
        #print(random.randint(0,100))
    #print(random.choice(buildlist))
main()

# below is code for getting a jpg from NASA URL - need to get RAW information with stream=True
url = demo_key url in ticks
r = request.get(url)
data = r.json()
print(data)

# get pic of the day
# perform get against the URL
pic_url = data['hdurl']
print(f"About to download the pic: {pic_url}")
r2 = requests.get(pic_url, stream=True)
# stored into memory location
print(r2.raw)
with open("space_image.jpg", "wb") as f: 
    shutil.copyfileobj(r2.raw, f)

urllib.request.urlretrieve(pic_url, "barn.jpg")
#urllib.request.urlretrieve(f'"{URL}", "barn.jpg"')

