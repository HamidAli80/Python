import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position_input = int(input('Enter position: '))
position = position_input - 1  # Convert to 0-based index

for i in range(count + 1):
    print(f"Retrieving: {url}")
    if i < count:  # Only process and follow links if not the last iteration
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
        except Exception as e:
            print(f"Error occurred: {e}")
            break
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        if not tags:
            print("No anchor tags found on the page.")
            break
        if position >= len(tags):
            print(f"Position {position_input} exceeds number of links ({len(tags)})")
            break
        next_url = tags[position].get('href', None)
        if next_url is None:
            print("No href found in the selected tag.")
            break
        url = urllib.parse.urljoin(url, next_url)

# Process the final URL to extract the name
if url.endswith('/'):
    url = url.rstrip('/')
last_part = url.split('/')[-1]
if '.' in last_part:
    base_name = last_part.split('.')[0]
else:
    base_name = last_part
name = base_name.split('_')[-1]

print(f"The answer to the assignment for this execution is \"{name}\".")