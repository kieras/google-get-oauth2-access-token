from time import time, sleep
from oauth2client import client

creds = client.GoogleCredentials.get_application_default()

creds = creds.create_scoped(['https://www.googleapis.com/auth/cloud-platform',
                             'https://www.googleapis.com/auth/datastore',
                             'https://www.googleapis.com/auth/cloudkms'])

access_token_info = None
expire_time = -1

while True:
    now = time()
    if not access_token_info or expire_time - now < 0:
        print('*****')
        print('Getting new access token...')
        access_token_info = creds.get_access_token()
        expire_time = now + access_token_info.expires_in
        print('New token: {}'.format(access_token_info))
        print('Expiring in {} seconds.'.format(expire_time - now))

    print('-----')
    print('Using token: {}'.format(access_token_info))
    print('Making the api call at {}'.format(str(now)))
    print('Expiring in {} seconds.'.format(expire_time - now))
    sleep(5)
