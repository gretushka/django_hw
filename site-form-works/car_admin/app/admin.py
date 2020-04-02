from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')
    list_filter = ['brand']
    search_fields = ('brand', 'model')




class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    list_filter = ['car']
    search_fields = ('title',)
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
