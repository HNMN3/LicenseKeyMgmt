import requests
from uuid import getnode


def check_license_key():
    server_url = 'http://127.0.0.1'
    license_key = open('license.txt').read().strip()
    hw_id = getnode()
    data = {
        'license_key': license_key,
        'hw_id': hw_id
    }
    api_path = '/license/'
    response = requests.post(server_url + api_path, data=data)
    response_dict = {
        200: ("License Key verified successfully!!", True),
        201: ("License Key registered successfully!!", True),
        400: ("Invalid License Key!!", False),
        406: ("License Key already used!!", False),
    }

    status_code = response.status_code
    print(hw_id)
    print(license_key)
    print(status_code)
    if status_code in response_dict:
        msg, flag = response_dict[status_code]
    else:
        msg, flag = "Unknown Error!! Please contact Administrator!!", False
    print(msg)
    return flag


print(check_license_key())
