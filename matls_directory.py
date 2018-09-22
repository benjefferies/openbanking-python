import requests

url = "https://service.directory.ob.forgerock.financial:443/directory-services/api/matls/test"

response = requests.request("GET", url, cert=('public.pem', 'private.key'))

print(f'Status {response.status_code}')
print(f'Response {response.text}')
