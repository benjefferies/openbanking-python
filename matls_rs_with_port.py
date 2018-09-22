import requests

url = "https://rs.aspsp.ob.forgerock.financial:443/open-banking/mtlsTest"

response = requests.request("GET", url, cert=('public.pem', 'private.key'))

print(f'Status {response.status_code}')
print(f'Response {response.text}')
