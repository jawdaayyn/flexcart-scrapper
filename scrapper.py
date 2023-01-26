from selectorlib import Extractor
import requests 
import sys
from time import sleep
def main(url):

    if "amazon" in url:
        e = Extractor.from_yaml_file('amaz-selectors.yml')      
    elif "zalando" in url:
        e = Extractor.from_yaml_file('zalando-selectors.yml')  
    elif "decathlon" in url:
        e = Extractor.from_yaml_file('deca-selectors.yml') 
    elif "fnac" in url:
        e = Extractor.from_yaml_file('fnac-selectors.yml') 
    elif "nike" in url:
        e = Extractor.from_yaml_file('nike-selectors.yml')
    elif "cdiscount" in url:
        e = Extractor.from_yaml_file('cdis-selectors.yml')  
    elif "micromania" in url:
        e = Extractor.from_yaml_file('micro-selectors.yml')  
    else:
        sys.exit("Site non géré")
    
    data = scrape(url, e)

    if data:

        #recup url
        data["url"] = url
        print(data)
        #recup prix
        data["price"] = data["price"].replace('\xa0', ' ')

        #creer nouveau produit et envoyer dans firebase
        print("Successfully saved")
        return(data)
    else:
        print("Error")

""" 
# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml') 
"""

def scrape(url, e):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        return None
    # Pass the HTML of the page and create 

    return e.extract(r.text)

if __name__=="__main__":
    main()