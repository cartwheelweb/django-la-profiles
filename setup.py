from distutils.core import setup

setup(name='django-la-profiles',
      version='0.3',
      description='User-profile application for Django',
      author='Daniel Greenfeld',
      author_email='pydanny@gmail.com',
      url='http://www.github.com/cartwheelweb/django-la-profiles/',
      #download_url='http://www.github.com/cartwheelweb/django-la-profiles/',
      packages=['profiles'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
