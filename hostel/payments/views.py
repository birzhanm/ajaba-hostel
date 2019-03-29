from django.shortcuts import render
from django.conf import settings
import stripe

stripe_pub = settings.STRIPE_PUBLIC_KEY
stripe_private = settings.STRIPE_PRIVATE_KEY

stripe.api_key = stripe_private

# Create your views here.
def checkin(request):
    context = {'stripe_pub': stripe_pub}
    return render(request, 'payments/checkin.html', context)

def process_payment(request):
    amount = 500

    customer = stripe.Customer.create(
        email=request.POST['stripeEmail'],
        source=request.POST['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Sample charge'
    )
    return render(request, 'success.html')
