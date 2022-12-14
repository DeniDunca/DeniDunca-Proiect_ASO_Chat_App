from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Feed
from .models import Room
from .models import Message

admin.site.register(Feed)
admin.site.register(Room)
admin.site.register(Message)
