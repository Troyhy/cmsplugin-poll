from django.template import Library
from django.template.loader import render_to_string
from cmsplugin_poll.models import Poll

register = Library()

@register.simple_tag
def get_latest_polls(count=5):
    polls = Poll.objects.all().order_by("-pub_date")[:5]
    return render_to_string("cmsplugin_poll/latest_polls.html", {
            "polls" : polls
            })

@register.simple_tag
def get_choice_rate(poll, choice):
    return "%d%%" % poll.getrate(choice)
