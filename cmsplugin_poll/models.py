from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class Poll(models.Model):
    question = models.CharField(_('question'), max_length=300)
    pub_date = models.DateTimeField(_('date published'))
    close_date = models.DateTimeField(_('date closed'), null=True)

    class Meta:
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')
        ordering = ('-pub_date',)

    def __unicode__(self):
        return unicode(self.question)

    def __repr__(self):
        return unicode(self)

    @models.permalink
    def get_absolute_url(self):
        return ('cmsplugin_poll.views.detail', (self.id,))

    @property
    def votes(self):
        return self.choice_set.aggregate(models.Sum('votes'))['votes__sum']

    def getrate(self, choice):
        total = self.votes
        if not total:
            return total
        return 100.0 * choice.votes / float(total)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, verbose_name=_('poll'))
    choice = models.CharField(_('choice'), max_length=200)
    votes = models.IntegerField(_('votes'), default=0)

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')

    def __unicode__(self):
        return '%s (%s)' % (self.choice, self.poll)


class PollPlugin(CMSPlugin):
    poll = models.ForeignKey(Poll, verbose_name=_("Poll to display"))

    class Meta:
        verbose_name = _('Poll plugin')
        verbose_name_plural = _('Poll plugins')

    def __unicode__(self):
        return self.poll.question

    def __str__(self):
        return self.poll.question
