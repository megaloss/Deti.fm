import csv
import urllib.request
with open('cms_scrape.csv', newline='') as f:
    reader = csv.reader(f)
    f.readline()
    for row in reader:
        #r = requests.get(row[1], allow_redirects=True)
        print("Downloading " + row[0]+".mp3")
        #open(row[0]+'.mp3, 'w').write(r.content)
        urllib.request.urlretrieve(row[1], row[0]+".mp3")
f.close()
