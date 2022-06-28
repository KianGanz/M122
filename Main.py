# See your keys here: https://dashboard.stripe.com/apikeys

stripe.PaymentIntent.create(
  amount=1099,
  currency='chf',
  payment_method_types=['card'],
)