import requests
from flask import Flask, render_template, redirect, url_for, session
from config import Config
import json


from forms import PaymentForm
from additional import BASE_CURRENCIES,\
    CREATE_BILL_URL, CREATE_INVOICE_URL, make_sign_string

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def main_form():
    form = PaymentForm()
    if form.validate_on_submit():
        currency = BASE_CURRENCIES.get(form.currency.data)
        # eur
        if currency == 978:
            # create sign string
            data = {
                'amount': form.amount.data,
                'currency': currency,
                'shop_id': 5,
                'shop_order_id': 4126
            }
            sign = make_sign_string(data)
            data['description'] = form.description.data
            data['sign'] = sign
            session['data'] = data
            return redirect(url_for('accept_usd'))
        # usd
        elif currency == 840:
            # create sign string
            data = {
                'shop_amount': str(form.amount.data),
                'shop_currency': 840,
                'shop_id': '5',
                'shop_order_id': '123456',
                'payer_currency': currency,
            }
            sign = make_sign_string(data)
            data['description'] = form.description.data
            data['sign'] = sign
            data = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            response = requests.post(CREATE_BILL_URL, data=data, headers=headers)
            response_data = json.loads(response.content.decode('utf-8'))
            if response_data['result']:
                url = response_data['data']['url']
                return redirect(url)
        # rub
        elif currency == 643:
            data = {
                "amount": str(form.amount.data),
                "payway": "payeer_rub",
                'shop_id': 5,
                'shop_order_id': 123456,
                "currency": str(currency)
            }
            sign = make_sign_string(data)
            data['description'] = form.description.data
            data['sign'] = sign
            data = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            response = requests.post(CREATE_INVOICE_URL, data=data, headers=headers)
            response_data = json.loads(response.content.decode('utf-8'))
            if response_data['result']:
                session['data'] = response_data
                return redirect(url_for('accept_rub'))
    return render_template('base_form.html',  form=form)


@app.route('/accept_usd')
def accept_usd():
    data = session.pop('data', None)
    return render_template('accept_usd.html', data=data)


@app.route('/accept_rub')
def accept_rub():
    data = session.pop('data', None)['data']
    method = data['method']
    data = data['data']
    return render_template('accept_rub.html', data=data, method=method)


if __name__ == '__main__':
    app.run()

