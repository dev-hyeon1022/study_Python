import json
import platform
import random

import requests
import config
import auth


def password_phone(from_number : str):
    # 랜덤 값 생성후 그걸 리스트로 담고 그걸 조인해서 6자리 문자열 생성하기

    default_agent = {
        'sdkVersion': 'python/4.2.0',
        'osPlatform': platform.platform() + " | " + platform.python_version()
    }


    url = "http://api.coolsms.co.kr/messages/v4/send"
    headers = auth.get_headers('NCSFS6ET7EKXHOPT', '2MQGWQABDAFY1KWN8QFIVBL3T2ZOSXNT')

    data = {
        "message": {
            "to": "01012341234",
            "from": from_number,
            "subject": "인증번호",
            "text": "테스트"
        }
    }
    print(json.dumps(data, ensure_ascii=False))
    response = requests.post(config.get_url('/messages/v4/send'),
                             headers=auth.get_headers(config.api_key, config.api_secret),
                             json=data)
    print(response.status_code)
    print(response.text)
