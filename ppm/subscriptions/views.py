# views.py

from django.shortcuts import render
import stripe
from djstripe.models import Product, Price


def checkout(request):
    stripe.api_key = 'sk_test_51MivDcBFBSPM7JAl8dagD6ybTE8xenpMv5yFEp16KnqAwIyzURMLkfnGaZKGija4TeqrFHh6SVvyG20g7TEfhWKP00PdedNnYY'

    # create a new product and price
    product = Product.create(name='My Product')
    price = Price.create(unit_amount=1000, currency='usd', product=product)

    # create a new PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=price.unit_amount,
        currency=price.currency,
        description=product.name,
        metadata={'integration_check': 'accept_a_payment'},
    )

    # render the checkout page with the PaymentIntent's client_secret
    return render(request, 'checkout.html', {'client_secret': intent.client_secret})
