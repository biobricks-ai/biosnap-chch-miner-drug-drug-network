import requests
import re

url = "https://snap.stanford.edu/biodata/datasets/10001/10001-ChCh-Miner.html"
try:
    r = requests.get(url)
    if r.status_code == 200:
        print(f"Got page: {url}")
        links = re.findall(r'href=[\'"]?([^\'" >]+)', r.text)
        for link in links:
            if link.endswith(".gz") or "ChCh" in link:
                print(f"Found link: {link}")
    else:
        print(f"Failed to get page: {r.status_code}")
except Exception as e:
    print(e)
