from setuptools import setup, find_packages
import os

setup(
    name = "cmsplugin-poll",
    packages = find_packages(),
    package_data = {
        'cmsplugin_poll': [
            'templates/cmsplugin_poll/*.html'
        ]
    },
    version = "0.2",
    description = "Simple poll plugin for django-cms 2.2",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = "Antoine Nguyen",
    author_email = "tonio@ngyn.org",
    url = "http://bitbucket.org/tonioo/cmsplugin-poll",
    license = "BSD",
    keywords = ["django", "django-cms", "poll"],
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django"
        ],
    include_package_data = True,
    zip_safe = False,
    install_requires = ['setuptools', 'django-cms', 'south'],
   ) 
