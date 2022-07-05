# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv('stripe.api_key'))


stripe.PaymentIntent.create(
  amount=1099,
  currency='chf',
  payment_method_types=['card'],
)