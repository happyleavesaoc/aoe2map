from django.contrib import admin

from mapsapp.models import Image, Rms, Tag, VersionTag, Collection, Profile

admin.site.register(VersionTag)
admin.site.register(Tag)
admin.site.register(Rms)
admin.site.register(Image)
admin.site.register(Collection)
admin.site.register(Profile)
