import requests
response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls') # /repos/{owner}/{repo}/pulls    https://api.github.com/repos/OWNER/REPO/pulls
print(response) # u get a class object
#print(response.json()) # automatically taken care of converting json to list of dicts
print(response.status_code) # status code of the connection

for i in range(0,len(response.json())):
    print(response.json()[i]['user']['login'])