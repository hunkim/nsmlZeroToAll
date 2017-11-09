"""Logging with nsml
=====================

This example shows how easy it is to log arbitrary values during program
execution. These logs can be visualized automatically and are stored for later
reference.

"""


import nsml
import time
from random import randint

# nsml plot -f [NAME]
for epoch in range(2000):
    time.sleep(1)
    nsml.report(epoch=epoch,
                train__acc=randint(0, 9),
                train__loss=randint(0, 9))
