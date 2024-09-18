from django.contrib import admin
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'user', 'expiration', 'create_at')
    list_filter = ("user", "expiration")
    search_fields = ['order_code', 'user']
admin.site.register(Order, OrderAdmin)