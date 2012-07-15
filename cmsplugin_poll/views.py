from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from models import Poll, Choice


def index(request):
    polls = Poll.objects.iterator()
    c = RequestContext(request, {'polls': polls})
    return render_to_response('cmsplugin_poll/latest_polls.html', c)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    c = RequestContext(request, {'poll': poll})
    return render_to_response('cmsplugin_poll/detail.html', c)


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if poll.close_date is not None:
        messages.error(request, _("This poll is closed"))
    elif request.session.get("poll_%d" % poll.id, False):
        messages.error(request, _("You already vote for this poll"))
    else:
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, _("You didn't select a choice"))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            messages.info(request, _("Thank you for your vote"))
            request.session["poll_%d" % poll.id] = True
    url = request.POST.get('next', poll.get_absolute_url())
    return HttpResponseRedirect(url)


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    c = RequestContext(request, {'poll': poll})
    return render_to_response('cmsplugin_poll/results.html', c)
