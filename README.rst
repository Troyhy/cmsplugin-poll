Django CMS simple poll plugin
=============================

Simple poll plugin for `Django CMS <http://django-cms.org>`_.

Requirements
------------

* `Django CMS >= 2.2 <http://django-cms.org>`_
* `South >= 0.7.3 <http://south.aeracode.org/>`_

Installation
------------

#. Open the *settings.py* file and add ``cmsplugin_poll`` to the
``INSTALLED_APPS`` variable.

#. Run the following command::

   $ ./manage.py migrate

#. Open the *urls.py* file and add the following to ``urlpatterns``::

   url(r'^poll/', include('cmsplugin_poll.urls')),

