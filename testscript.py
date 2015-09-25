#!/usr/bin/env python
import flock # for binary probably need fcntl
import time

# explanation of 'with' http://effbot.org/zone/python-with-statement.htm
with open('tempfile', 'w') as f:
    blocking_lock = flock.Flock(f, flock.LOCK_EX)

    with blocking_lock:
        print "have lock"
        time.sleep(10)

    print "done with lock"
