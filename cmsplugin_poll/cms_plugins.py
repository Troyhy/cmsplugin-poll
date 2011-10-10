from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_poll.models import *
from django.utils.translation import ugettext as _

class CMSPollPlugin(CMSPluginBase):
    model = PollPlugin
    name = _("Simple poll plugin")
    render_template = "cmsplugin_poll/detail.html"

    def render(self, context, instance, placeholder):
        context.update({
                "poll" : instance.poll,
                })
        return context

plugin_pool.register_plugin(CMSPollPlugin)
