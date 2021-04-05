import urllib.parse
import base64

fullSearchURI = "https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json"

apiKey = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
apiKeySecret = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

def get_bearer_token():
  bearer_token_credentials = get_bearer_token_credentials(apiKey, apiKeySecret)
  return get_bearer_token(bearer_token_credentials)

def get_bearer_token_credentials(key, secret):
  url_encoded_credentials = urllib.parse.quote(key) + ":" + urllib.parse.quote(secret)

  return base64.b64encode(url_encoded_credentials.encode('ascii'))
def get_bearer_token(credentials):
    pass

creds = get_bearer_token_credentials(apiKey, apiKeySecret)
print(creds) #== "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
