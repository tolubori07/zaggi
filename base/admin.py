from django.contrib import admin
from .models import Items,User,ItemView
# Register your models here.
admin.site.register(Items)
admin.site.register(User)
admin.site.register(ItemView)