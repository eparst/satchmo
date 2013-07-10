#!/usr/bin/env python

from setuptools import setup

setup(
    name='YourAppName',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.4.5','pycrypto','pyyaml','pil','django-threaded-multihost','django-app-plugins', #'django-app-plugins==0.1.2'
					'sorl-thumbnail','django-signals-ahoy',
					'django-livesettings','django-keyedcache','South','django-registration',
					'sphinx','docutils','fedex','suds','Reportlab'],
	scripts=['bin/clonesatchmo.py']
)
