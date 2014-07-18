pytz-memcache
=============

pytz with memcache modified to be hi performance that also works on GAE

( copied from pytz-2014.4 )


Usage
-----

 - unzip pytz-2014.4-py2.5.egg
 - delete *.pyc
 - zip recursive pytz/zoneinfo/ to zoneinfo.zip
 - copy zoneinfo.zip to application directory (current directory on GAE)
 - replace __init__.py open_resource function (in this repository)
 - zip pytz/ to pytz-2014.4-gae-py2.X.egg (without zoneinfo.zip)
 - copy pytz-2014.4-gae-py2.X.egg to application directory


Links
-----

 - https://github.com/HatsuneMiku/pytz-memcache
 - https://github.com/HatsuneMiku/pytz-memcache/wiki
 - https://pypi.python.org/pypi/pytz-memcache

