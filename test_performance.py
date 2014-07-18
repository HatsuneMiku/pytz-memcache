#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_performance
'''

import pytz
import calendar
import datetime
import time
import pprint

def inferTZ():
  '''not support summertime information yet'''
  result = []
  t = datetime.datetime.utcnow()
  d = datetime.datetime.now() - t
  # force microseconds=0 and last digit of seconds=0 (can use only TZ > GMT+0)
  d = datetime.timedelta(days=d.days,
    seconds=int(d.seconds / 10) * 10, microseconds=0)
  for tz_str in pytz.common_timezones: # (must modify pytz zoneinfo.zip on GAE)
    ptzi = pytz.timezone(tz_str)
    if pytz.utc.localize(t) - ptzi.localize(t) == d:
      result.append((tz_str, ptzi.tzname(t), ptzi.utcoffset(t), ptzi))
  return result

def test_performance():
  TZ = inferTZ()
  pprint.pprint(TZ)

if __name__ == '__main__':
  st = time.time()
  print 'start: %s' % st
  test_performance()
  et = time.time()
  print 'end: %s (%s)' % (et, et - st)
