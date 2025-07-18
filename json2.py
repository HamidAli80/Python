import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
# Extract the list of comments
comments = info.get('comments', [])
  
# Initialize counters
total_count = 0
count = 0
    
  # Iterate through each comment to sum the counts
for comment in comments:
    cnt = comment.get('count', 0)
    total_count += cnt
    count += 1
    
# Print the results
print('Count:', count)
print('Sum:', total_count)