pytz-memcache
=============

pytz with memcache modified to be high performance that also works on GAE

( copied from pytz-2014.4 )


Usage
-----

 - copy zoneinfo.zip to your application directory (current directory on GAE)
 - copy pytz-2014.4-gae-py2.X.egg to your application directory


```python
import os
import pytz
if 'SERVER_SOFTWARE' in os.environ.keys(): # on GAE
  from google.appengine.api import memcache
  from google.appengine.ext import webapp
else:
  import memcache

class GAEHandler(webapp.RequestHandler):
  def get(self, param):
    self.response.out.write(pytz.common_timezones)
```


Remarks
-------

 - 'zoneinfo.zip' must be in your application directory
 - memcached must be running on '127.0.0.1:11211' (local)
 -   (memcached has been running on GAE)
 - it takes about few seconds to run at the first time, but faster next
 - please delete key 'pytz_loaded' from cache when update pytz zoneinfo


Do It Yourself
--------------

 - unzip pytz-2014.4-py2.5.egg
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


Relations
---------

 - python-memcached (client OS independent) https://pypi.python.org/pypi/python-memcached/1.53
 - memcached (server for UNIX) http://memcached.org/
 - MemCacheD Manager (server for windows) http://allegiance.chi-town.com/MemCacheDManager.aspx

