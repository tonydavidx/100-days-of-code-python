import requests

url = "https://storage.bunnycdn.com/my-space/foodybite-free-ui-kit-for-adobe-xd/"

headers = {
    "Accept": "*/*",
    "AccessKey": "8fca02ad-f488-45f2-9656-acdb54e9659adbe2944c-236b-4c09-ae82-193091dcbe53"
}

response = requests.request("GET", url, headers=headers)

print(response.text)