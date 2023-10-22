#
# twitter requires a developer account to use api
# access token and access token secret are going to be in ENV vars
import os
import webbrowser
from twython import Twython # requires to be installed
#
# these tokens are used for oauth part
ACCESS_TOKEN = os.environ['TW_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TW_ACCESS_TOKEN_SECRET']
print(f"ACCESS TOKEN: {ACCESS_TOKEN}")
print(f"ACCESS TOKEN SECRET: {ACCESS_TOKEN_SECRET}")
temp_client = Twython(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
temp_creds = temp_client.get_authentication_tokens()
#
# Session token can be saved and reused(?)
# so if i have them already, I skip this part..
if os.environ.get('SESSION_ACCESS_TOKEN') == None or \
   os.environ.get('SESSION_ACCESS_TOKEN_SECRET') == None:
    #
    # we need to visit the url to get a pin code; this is MFA based
    # so human interaction is required    
    url = temp_creds['auth_url']
    print(f"Now visiting {url} to get the PIN code")
    webbrowser.open(url)
    PIN_CODE = input("please enter the PIN code: ")
    #
    # now we can use the pin code t get the actual tokens
    auth_client = Twython(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET,
                          temp_creds['oauth_token'],
                          temp_creds['oauth_token_secret'])
    #
    final_step = auth_client.get_authorized_tokens(PIN_CODE)
    SESSION_ACCESS_TOKEN = final_step['oauth_token']
    SESSION_ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']
    #
    #
    print("Getting sessions tokens:")
    print(f"SESSION_ACCESS_TOKEN: {SESSION_ACCESS_TOKEN}")
    print(f"SESSION_ACCESS_TOKEN_SECRET: {SESSION_ACCESS_TOKEN_SECRET}")
    print("You can save them and reuse to skip this process")
else:  
    print("Getting session tokens from ENV vars")
    SESSION_ACCESS_TOKEN = os.environ['TW_SESSION_ACCESS_TOKEN']
    SESSION_ACCESS_TOKEN_SECRET = os.environ['TW_SESSION_ACCESS_TOKEN_SECRET']  
#
# now create a client with all the tokens
twitter = Twython(ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET,
                  SESSION_ACCESS_TOKEN,
                  SESSION_ACCESS_TOKEN_SECRET)