from django.contrib import admin
from .models import FeeInvoice, Payment

admin.site.register(FeeInvoice)
admin.site.register(Payment)