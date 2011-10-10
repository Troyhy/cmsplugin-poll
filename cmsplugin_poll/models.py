from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

class Poll(models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    close_date = models.DateTimeField('date closed', null=True)

    def __unicode__(self):
        return unicode(self.question)

    def __repr__(self):
        return unicode(self)

    @property
    def votes(self):
        res = 0
        for c in self.choice_set.all():
            res += c.votes
        return res

    def getrate(self, choice):
        total = self.votes
        if not total:
            return total
        return choice.votes / float(total) * 100.0

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class PollPlugin(CMSPlugin):
    poll = models.ForeignKey(Poll, verbose_name=_("Poll to display"))

    def __unicode__(self):
        return self.poll.question

    def __str__(self):
        return self.poll.question

