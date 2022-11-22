from __future__ import absolute_import
from . import APP
import time


@APP.task(name="longtime_add")
def longtime_add():
    print("long time task begins")
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    return 12
