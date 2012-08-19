import datetime
from cmsplugin_poll.models import Poll, Choice, UserChoice
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


def make_closed(modeladmin, request, queryset):
    queryset['close_date'] = datetime.datetime.now()
make_closed.short_description = _("Close selected polls")


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


class UserChoiceInline(admin.TabularInline):
    model = UserChoice
    extra=0
    fields = ('get_user_name',)
    readonly_fields = ('get_user_name',)
    
class PollAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    fieldsets = [
        (None,                     {"fields": ["question", "track_user"]}),
        (_("Date information"),    {"fields": ["pub_date"]})
    ]
    inlines = [ChoiceInline,UserChoiceInline]
    actions = [make_closed]

    list_display = ("question", "pub_date", "votes", "close_date")
    list_filter = ["pub_date"]
    search_fields = ["question"]
    date_hierarchy = "pub_date"

admin.site.register(Poll, PollAdmin)
