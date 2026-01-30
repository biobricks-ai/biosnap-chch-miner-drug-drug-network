import requests

urls = [
    "https://snap.stanford.edu/biodata/datasets/10018/files/ChCh-Miner_miner-chem-chem.tsv.gz",
    "http://snap.stanford.edu/biodata/datasets/10018/files/ChCh-Miner_miner-chem-chem.tsv.gz",
    "https://snap.stanford.edu/biodata/datasets/10018/files/ChCh-Miner.tsv.gz",
    "https://snap.stanford.edu/biodata/datasets/10018/files/ChCh-Miner_drug-drug.tsv.gz",
    "https://snap.stanford.edu/biodata/datasets/10000/files/ChCh-Miner.tsv.gz"
]

for url in urls:
    try:
        r = requests.head(url)
        print(f"{url}: {r.status_code}")
    except Exception as e:
        print(f"{url}: Error {e}")
