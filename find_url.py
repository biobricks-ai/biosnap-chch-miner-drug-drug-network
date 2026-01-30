import requests
import re

url = "https://snap.stanford.edu/biodata/"
try:
    r = requests.get(url)
    if r.status_code == 200:
        print("Got index page")
        if "ChCh-Miner" in r.text:
            print("Found ChCh-Miner in text")
            # Extract links
            links = re.findall(r'href=[\'"]?([^\'" >]+)', r.text)
            for link in links:
                if "ChCh-Miner" in link:
                    print(f"Found link: {link}")
        else:
            print("ChCh-Miner not found in text")
            
        if "drug" in r.text.lower():
            print("Found 'drug' in text")
            
    else:
        print(f"Failed to get index page: {r.status_code}")

except Exception as e:
    print(e)
