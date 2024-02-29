from django.contrib import admin

from .models import User_registration, Add_movies, Category

# Register your models here.
admin.site.register(User_registration)
admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['movie_title','slug','category']
    list_editable = ['category']
    list_per_page = 20
admin.site.register(Add_movies,CategoryAdmin)


