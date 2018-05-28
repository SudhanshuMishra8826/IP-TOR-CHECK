import csv
import requests
ip=input("Enter the ip to be checked ")
flag=0
with requests.Session() as s:
    download = s.get('https://torstatus.blutmagie.de/ip_list_all.php/Tor_ip_list_ALL.csv')
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    tl = list(cr)
for row in tl:
    if row[0]==ip:
        flag=1
        break
if flag==1:
    print("ENTERED IP IS A TOR IP")
else:
    print("ENTERED IP IS NOT A TOR IP")

