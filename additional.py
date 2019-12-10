import hashlib


BASE_CURRENCIES = {
    'usd': 840,
    'rub': 643,
    'eur': 978
}

SECRET_KEY = 'SecretKey01'

PAYWAY = 'payeer_rub'

CREATE_BILL_URL = 'https://core.piastrix.com/bill/create'

CREATE_INVOICE_URL = 'https://core.piastrix.com/invoice/create'


def make_sign_string(data):

    data_keys = sorted(data.keys())

    gen_string = ''

    for idx, key in enumerate(data_keys):
        gen_string += str(data.get(key))
        # if not penultimate element
        if idx <= len(data_keys) - 2:
            gen_string += ':'
    gen_string += SECRET_KEY
    gen_string = gen_string.encode('utf-8')
    sign = hashlib.sha256(gen_string).hexdigest()
    return sign