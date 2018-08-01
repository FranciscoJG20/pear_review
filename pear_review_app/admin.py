from django.contrib import admin
from .models import Issue, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from pear_review_app.models import Pear

class PearInline(admin.StackedInline):
    model = Pear
    can_delete = False
    verbose_name_plural = 'pear'

class UserAdmin(BaseUserAdmin):
    inlines = [ PearInline,
    ]    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Registering Issue and Comment models here:
admin.site.register(Issue)
admin.site.register(Comment)


