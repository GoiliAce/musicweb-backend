from django.contrib import admin

from .models import *

admin.site.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'thumbnail', 'follow')
    list_filter = ('name', 'alias', 'thumbnail', 'follow')
    search_fields = ('name', 'alias', 'thumbnail', 'follow')
    ordering = ('name', 'alias', 'thumbnail', 'follow')
    filter_horizontal = ('songs',)
    # fields = ('name', 'alias', 'thumbnail', 'follow')
    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'alias', 'thumbnail', 'follow')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('songs',),
    #     }),
    # )

admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    list_filter = ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    search_fields = ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    ordering = ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    # fields = ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'thumbnail_url', 'descripton', 'date_create', 'like')
    #     }),
    # )
admin.site.register(Artistalbum)
    
admin.site.register(Artistsong)
admin.site.register(Category)
admin.site.register(Categorysong)
admin.site.register(Song)
admin.site.register(Playlistbyusersong)
admin.site.register(Playlistsong)
admin.site.register(Playlistuser)
admin.site.register(Topic)
admin.site.register(Usersongs)
admin.site.register(User)
admin.site.register(Playlistbyuser)
admin.site.register(Playlist)

# admin.site.register(Userfollowartist)
# admin.site.register(Userfollowcate)
# admin.site.register(Userfollowsong)
# admin.site.register(Userlikealbum)
# admin.site.register(Userlikecate)
# admin.site.register(Userlikesong)
# admin.site.register(Userplaylist)
# admin.site.register(Userplaylistsong)
# admin.site.register(Userprofile)
# admin.site.register(Userprofileimage)
# admin.site.register(Userprofileimageuser)
# admin.site.register(Userprofileuser)
