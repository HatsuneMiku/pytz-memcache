pytz-memcache
=============

latest version at https://github.com/HatsuneMiku/pytz-memcache

pytz with memcache modified to be high performance that also works on GAE

( copied from pytz-2014.4 )


Usage
-----

 - copy zoneinfo.zip to your application directory (current directory on GAE)
 - copy pytz-2014.4-gae-py2.X.egg to your application directory


```python
import os

if 'SERVER_SOFTWARE' in os.environ.keys(): # on GAE
  from google.appengine.api import memcache
  from google.appengine.ext import webapp
  # use zoneinfo.zip on current directory
  # pytz-2014.4-py2.5.egg does not work on GAE (pytz.common_timezones is [])
  sys.path.append('pytz-2014.4-gae-py2.5.egg')
else:
  import memcache

import pytz

class GAEHandler(webapp.RequestHandler):
  def get(self, param):
    self.response.out.write(pytz.common_timezones)
```


Remarks
-------

 - 'zoneinfo.zip' must be in your application directory
 - memcached must be running on '127.0.0.1:11211' (for local test only)
 -   (memcached has been running on GAE)
 - it takes about few seconds to run at the first time, but faster next
 - please delete key 'pytz_loaded' from cache when update pytz zoneinfo


Do It Yourself
--------------

 - unzip pytz-2014.4-py2.X.egg
 - delete *.pyc
 - zip recursive pytz/zoneinfo/ to zoneinfo.zip
 - copy zoneinfo.zip to your application directory (current directory on GAE)
 - replace __init__.py open_resource function (in this repository)
 - zip pytz/ to pytz-2014.4-gae-py2.X.egg (without zoneinfo.zip)
 - copy pytz-2014.4-gae-py2.X.egg to your application directory


Links
-----

 - https://github.com/HatsuneMiku/pytz-memcache
 - https://github.com/HatsuneMiku/pytz-memcache/wiki
 - https://pypi.python.org/pypi/pytz-memcache


Requirements
------------

 - pytz (included)
 - python-memcached (for local test only)


Relations
---------

 - pytz https://pypi.python.org/pypi/pytz
 - python-memcached (client OS independent) https://pypi.python.org/pypi/python-memcached/1.53
 - GAE https://appengine.google.com/
 - memcached (server for UNIX) http://memcached.org/
 - MemCacheD Manager (server for windows) http://allegiance.chi-town.com/MemCacheDManager.aspx

