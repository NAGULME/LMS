from django.contrib import admin

# Register your models here.

from .models import *
class what_you_learn_TabularInline(admin.TabularInline)
    model = what_you_learn
    class= Requirements_TabularInline(admin.TabularInline)
model =Requirements

class video_TabularInline(admin.TabularInline):
    model = video 

class course_admin(admin.ModelAdmin):
    inlines=( what_you_learn_TabularInline,Requirements_TabularInline,video_TabularInline)

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,course_admin)
admin.site.register(Level)
admin.site.register(what_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
