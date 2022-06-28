# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_51LFeLQIPHMm43ITmL8NdxFkRDd2S82yh98lHe9lCJTRf8BPRsN5sa9LRkqItnawVkkATQAwOHSZb2p3pd5PrFa3F00aDg08c6b'

stripe.PaymentIntent.create(
  amount=1099,
  currency='chf',
  payment_method_types=['card'],
)