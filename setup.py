import os
from setuptools import setup


# Utility function to read the README file
# Easier than line wrapping a long string...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "autologin",
    version = "0.1.5",
    author = "Alejandro Caceres, Luke Maxwell",
    author_email = "lukemaxwellshouse@gmail.com",
    description = ("A utility for finding login links, forms and autologging "
                   "into websites with a set of valid credentials."),
    license = "MIT",
    keywords = "login, automated, spider",
    url = "https://github.com/TeamHG-Memex/autologin",
    packages=['autologin'],
    include_package_data = True,
    python_requires='>=3.8',
    install_requires = [
        'six',
        'lxml>=4.9.0',
        'Flask>=2.3.0',
        'Flask-Admin>=1.6.0',
        'Flask-SQLAlchemy>=3.0.0',
        'Flask-WTF>=1.0.0',
        'WTForms>=3.0.0',
        'scrapy>=2.11.0',
        'numpy>=1.24.0',  # These 3 are formasaurus deps, make sure we always have them
        'scipy>=1.10.0',
        'scikit-learn>=1.3.0',
        'formasaurus[with_deps]>=0.8',
        'scrapy-splash>=0.9.0',
        'crochet>=2.0.0',
        'requests>=2.31.0',
    ],
    entry_points = {
        'console_scripts': [
            'autologin = autologin.autologin:main',
            'autologin-server = autologin.server:main',
            'autologin-http-api = autologin.http_api:main',
            'autologin-init-db = autologin.app:init_db',
        ]
    },
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
