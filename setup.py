# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the gettext helper script for Sphinx_ .

.. _Sphinx: http://sphinx.pocoo.org/

This script enable you to update and build gettext message catalogs more easy::

   # update and merge PO file from POT file (pot file is generated from Sphinx)
   $ sphinx-gettext-helper --potdir=_build/locale --update

   # build MO file from translated PO file
   $ sphinx-gettext-helper --potdir=_build/locale --build

'''

requires = ['Sphinx>=1.1.0']

setup(
    name='sphinx-gettext-helper',
    version='0.2.1',
    url='http://bitbucket.org/tk0miya/sphinx-gettext-helper',
    download_url='http://pypi.python.org/pypi/sphinx-gettext-helper',
    license='BSD',
    author='Takeshi Komiya',
    author_email='i.tkomiya@gmail.com',
    description='gettext helper script for Sphinx',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinx_gettext_helper'],
    entry_points="""
        [console_scripts]
        sphinx-gettext-helper = sphinx_gettext_helper.command:main
    """,
)
