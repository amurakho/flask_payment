from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired


class PaymentForm(FlaskForm):
    amount = FloatField('Сумма оплаты', [DataRequired()])
    currency = SelectField('Валюта', choices=[('usd', 'USD'), ('eur', 'EUR'), ('rub', 'RUB')])
    description = StringField('Описание товара', validators=[DataRequired()])
    submit = SubmitField('Оплатить')




# import requests
# from flask import Flask, render_template, redirect, url_for, session
# from config import Config
# import json
# import hashlib
#
#
# from forms import PaymentForm
# from additional import BASE_CURRENCIES, PAYWAY,\
#     CREATE_BILL_URL, BILL_REQUEST_BODY, make_sign_string, SECRET_KEY
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def main_form():
#     form = PaymentForm()
#     if form.validate_on_submit():
#         currency = BASE_CURRENCIES.get(form.currency.data)
#         # eur
#         if currency == 978:
#             # create sign string
#             data = {
#                 'amount': form.amount.data,
#                 'currency': currency,
#                 'shop_id': 5,
#                 'shop_order_id': 4126
#             }
#             sign = make_sign_string(data)
#             data['description'] = form.description.data
#             data['sign'] = sign
#             session['data'] = data
#             return redirect(url_for('accept_usd'))
#         # usd
#         # elif currency == 840:
#         #     # create sign string
#         #     data = {
#         #         'shop_amount': form.amount.data,
#         #         'shop_currency': 840,
#         #         'shop_id': 112,
#         #         'shop_order_id': 4239,
#         #         'payer_currency': currency,
#         #     }
#         #     sign = make_sign_string(data)
#         #     data['description'] = form.description.data
#         #     data['sign'] = sign
#         #     data = json.dumps(data)
#         #     headers = {'Content-type': 'application/json'}
#         #     response = requests.post(CREATE_BILL_URL, data=data, headers=headers)
#         # #     if response.status_code == 200:
#         # #         response_data = json.loads(response.content.decode('utf-8'))
#         # #         print(response_data)
#         # #         # if response_data['result']:
#         # #         #     url = response_data['data']['url']
#         # #         #     return redirect(url)
#         # # # rub
#         # elif currency == 643:
#         #     data = {
#         #         "amount": form.amount.data,
#         #         "payway": "payeer_rub",
#         #         'shop_id': 5,
#         #         'shop_order_id': 123456,
#         #         "currency": currency,
#         #     }
#         #     sign = make_sign_string(data)
#         #     data['description'] = form.description.data
#         #     data['sign'] = sign
#         #     data = json.dumps(data)
#         #     headers = {'Content-type': 'application/json'}
#         #     response = requests.post(CREATE_BILL_URL, data=data, headers=headers)
#         #     print(response.content)
#     return render_template('base_form.html',  form=form)
#
#
# @app.route('/accept_usd')
# def accept_usd():
#     data = session.pop('data', None)
#     return render_template('accept_usd.html', data=data)
#
#
# if __name__ == '__main__':
#     app.run()

