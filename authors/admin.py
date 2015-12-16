from django.contrib import admin
from authors.models import UserProfile, Abstract
from django.contrib.auth.models import User


class AbstractAdmin(admin.ModelAdmin):
    list_display = ( 'short_title', 'view_id', 'view_link', 'affiliation', 'status', 'delivery','delivery_decision', 'date', 'author_registered')

    def affiliation(self, obj):
        return ("%s" % obj.author.affiliation)
    affiliation.admin_order_field='author__affiliation'

    def short_title(self, obj):
        return ("%s ..." % (obj.title[:50]))
    short_title.short_description = 'Title'

    def view_link(self, obj):
        return u"<a href='/programme/profiles/%d'>%s</a>" % (obj.author.user.id, obj.author.user.last_name)
    view_link.short_description = 'author'
    view_link.admin_order_field = 'author__user__last_name'
    view_link.allow_tags = True

    def view_id(self, obj):
        return u"<a href='/media/%s' target='_blank'>%s</a>" % (obj.upload, obj.unique_id)

    view_id.short_description = 'ID'
    view_id.admin_order_field='unique_id'
    view_id.allow_tags = True

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'affiliation', 'twitter')
    


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Abstract, AbstractAdmin)


