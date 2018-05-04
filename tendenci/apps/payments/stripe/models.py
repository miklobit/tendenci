from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from tendenci.apps.perms.models import TendenciBaseModel


class StripeAccount(TendenciBaseModel):
    """
    A Stripe connected account
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="stripe_accounts")
    account_name = models.CharField(max_length=250, default='')
    email = models.CharField(max_length=200, default='')
    default_currency = models.CharField(max_length=5, default='usd')
    country = models.CharField(max_length=5, default='US')
    stripe_user_id = models.CharField(_(u'Stripe user id'), max_length=200, unique=True)
    
    scope = models.CharField(max_length=20)
    token_type = models.CharField(max_length=20)
    refresh_token = models.CharField(max_length=200)
    livemode_access_token = models.CharField(max_length=200)
    testmode_access_token = models.CharField(max_length=200)
    livemode_stripe_publishable_key = models.CharField(max_length=200)
    testmode_stripe_publishable_key = models.CharField(max_length=200)
