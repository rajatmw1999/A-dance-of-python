import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
# payload = "client_id%0A=###################&redirect_uri=#################%2F&client_secret=##############&code={}&grant_type=authorization_code&undefined=".format(code)
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache"
#     }
response = requests.get(url)
response = response.json()
print(response["userId"])

# https://realpython.com/python-requests/