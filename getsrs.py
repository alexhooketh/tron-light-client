import requests, base58
open("srs.txt", "w").write("\n".join([base58.b58decode(x["address"])[:21].hex() for x in requests.get("https://apilist.tronscanapi.com/api/pagewitness?witnesstype=0")["data"][:128]]))