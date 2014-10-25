import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='feedme',
    version='1.4.0',
    author='dotkom',
    author_email='dotkom@online.ntnu.no',
    packages=['feedme'],
    license='BSD License',  # example license
    description='Food ordering management for django',
    long_description='A food ordering management system for Django.\n
    This project was started to help \'dotKom\' with ordering food for their work nights.\n
    Check out the github repo for installation instructions.',
    url='http://online.ntnu.no/feedme',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
)
