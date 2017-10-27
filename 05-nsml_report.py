import nsml
import time
from random import randint

# nsml plot -f [NAME]
for epoch in range(2000):
    time.sleep(1)
    nsml.report(epoch=epoch,
                train__acc=randint(0, 9),
                train__loss=randint(0, 9))