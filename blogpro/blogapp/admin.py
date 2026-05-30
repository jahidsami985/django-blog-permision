from django.contrib import admin
from .models import MenuList, UserPermission, Category,Post

# Register your models here.
admin.site.register(MenuList)
admin.site.register(UserPermission) 
admin.site.register(Category)
admin.site.register(Post)
