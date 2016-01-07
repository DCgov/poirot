try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README_PYPI.rst') as file:
    long_description = file.read()

setup(name='poirot',
	  version='0.0.22',
	  author='Emanuel Feld',
	  author_email='elefbet@gmail.com',
	  description="Investigate a Git repository's revision history to find text patterns.",
	  long_description=long_description,
	  url='https://github.com/dcgov/poirot',
	  license='https://raw.githubusercontent.com/DCgov/poirot/master/LICENSE.md',
	  packages=['poirot'],
	  install_requires=['tqdm>=3.4.0', 'Jinja2>=2.8', 'regex>=2015.11.22'],
	  test_suite='nose.collector',
	  tests_require=['nose-progressive'],
	  classifiers=[
	  	'Environment :: Console',
	  	'Intended Audience :: Developers',
	  	'Development Status :: 3 - Alpha',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
	  	'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5'
	  ],
	  include_package_data=True,
	  entry_points = {
	  	'console_scripts': [
	  		'poirot=poirot.commands:poirot',
	  		]
	  },
	  zip_safe=False)
