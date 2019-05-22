from django.contrib import admin

from blogging.models import Post, Category, MediumClass


class MediumClassInline(admin.TabularInline):
    model = MediumClass
    extra = 1

#You’ll need to create a customized ModelAdmin.  class for the Post and Category models.
class PostAdmin(admin.ModelAdmin):
    inlines = [MediumClassInline,]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MediumClass)