import requests, json

from dateutil.parser import parse
acc_url = "https://api.github.com/users/19521242bao"
 
acc_info = json.loads(requests.get(acc_url).text)
 

print(acc_info['created_at'])
 
print(acc_info['updated_at'])
 
print(parse(acc_info['created_at']).month)
repos_url="https://api.github.com/users/19521242bao/repos"
repos_info = json.loads(requests.get(repos_url).text)
repos_names = [repo["name"] for repo in repos_info]
 
print(repos_names)