from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from models import *

def index(request):
    polls = Poll.objects.all().order_by("-pub_date")
    return render_to_response("cmsplugin_poll/latest_polls.html", {
            "polls" : polls
            })

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("cmsplugin_poll/detail.html", {"poll" : p},
                              context_instance=RequestContext(request))

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    if p.close_date is not None:
        messages.error(request, _("This poll is closed"))
    elif request.session.get("poll_%d" % p.id, False):
        messages.error(request, _("You already vote for this poll"))
    else:
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, _("You didn't select a choice"))
        else:
            selected_choice.votes += 1
            selected_choice.save()
            messages.info(request, _("Thank you for your vote"))
            request.session["poll_%d" % p.id] = True
    return HttpResponseRedirect(reverse('cmsplugin_poll.views.results', 
                                        args=(p.id,)))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('cmsplugin_poll/results.html', {'poll': p},
                              context_instance=RequestContext(request))

