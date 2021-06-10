from django.contrib import admin

from .models import Homeaddr, Product,Contact,Orders,OrderUpdate
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Homeaddr)