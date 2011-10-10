import datetime
from cmsplugin_poll.models import Poll, Choice
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

def make_closed(modeladmin, request, queryset):
    queryset.update(close_date=datetime.datetime.now())
make_closed.short_description = _("Close selected polls")

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {"fields": ["question"]}),
        ("Date information",    {"fields": ["pub_date"]})
        ]
    inlines = [ChoiceInline]
    actions = [make_closed]

    list_display = ("question", "pub_date", "votes", "close_date")
    list_filter = ["pub_date"]
    search_fields = ["question"]
    date_hierarchy = "pub_date"

admin.site.register(Poll, PollAdmin)
