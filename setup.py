from setuptools import setup, find_packages

setup(name='pocketsnack',
      version='2.1.0',
      url='https://hughrundle.net',
      license='GPL-3.0-or-later',
      packages=find_packages(),
      scripts=['bin/pocketsnack'],
      install_requires=['request'],
      zip_safe=False,
      author='Hugh Rundle',
      author_email='hugh@hughrundle.net',
      description='A command line package for managing Pocket accounts.',
      keywords='pocket, pocket api',
      project_urls={
        'Source Code': 'https://github.com/hughrun/pocketsnack',
        'Documentation': 'https://github.com/hughrun/pocketsnack'
      }
)
