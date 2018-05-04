from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from tendenci.apps.perms.admin import TendenciBaseModelAdmin
from models import StripeAccount

class StripeAccountAdmin(TendenciBaseModelAdmin):
    list_display = ('account_name', 'email', 'default_currency', 'stripe_user_id', 'scope',
                     'status_detail')
    list_filter = ('status_detail',)
    search_fields = ('account_name', 'email')
    readonly_fields=('stripe_user_id', 'scope')
    fields = ('account_name', 'email', 'default_currency',
              'stripe_user_id', 'scope',
            'status_detail')
    ordering = ['-update_dt']

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('stripe_connect.authorize'))


admin.site.register(StripeAccount, StripeAccountAdmin)