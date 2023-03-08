import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import View


class CreateSubscriptionView(View):
    def post(self, request):
        # Get the Stripe API key from settings
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Create a new subscription for the user
        subscription = stripe.Subscription.create(
            customer=request.user.stripe_customer_id,
            items=[
                {
                    "price": request.POST.get("price_id"),
                },
            ],
        )

        # Save the subscription ID to the user's profile
        request.user.subscription_id = subscription.id
        request.user.save()

        return redirect("home")


class UpdateSubscriptionView(View):
    def post(self, request):
        # Get the Stripe API key from settings
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the new price ID from the form data
        new_price_id = request.POST.get("price_id")

        # Get the user's subscription ID
        subscription_id = request.user.subscription_id

        # Update the subscription with the new price
        subscription = stripe.Subscription.modify(
            subscription_id,
            items=[
                {
                    "id": subscription["items"]["data"][0]["id"],
                    "price": new_price_id,
                },
            ],
        )

        return redirect("home")


class CancelSubscriptionView(View):
    def post(self, request):
        # Get the Stripe API key from settings
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the user's subscription ID
        subscription_id = request.user.subscription_id

        # Cancel the subscription
        stripe.Subscription.delete(subscription_id)

        # Remove the subscription ID from the user's profile
        request.user.subscription_id = None
        request.user.save()

        return redirect("home")
