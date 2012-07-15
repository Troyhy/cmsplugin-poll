from django.template import Library
from django.template.loader import render_to_string
from cmsplugin_poll.models import Poll

register = Library()


@register.simple_tag
def get_latest_polls(count=5):
    "FIXME: I'm useless!"
    polls = Poll.objects.all()[:5]
    return render_to_string("cmsplugin_poll/latest_polls.html", {
            "polls": polls
            })


@register.simple_tag
def get_choice_rate(poll, choice):
    return "%d%%" % poll.getrate(choice)


@register.assignment_tag
def show_results(request, poll):
    poll_is_closed = poll.close_date is not None
    session_has_voted = request.session.get("poll_%d" % poll.id, False)
    return poll_is_closed or session_has_voted
