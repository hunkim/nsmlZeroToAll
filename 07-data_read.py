"""Accessing datasets with nsml
==================================

Machine learning relies on data. This example shows how to upload datasets to
the nsml cloud as well as how to access them later for training.

"""

import os
import numpy as np

# 1. Push data
#   $ nsml dataset push diabetes data/
# 2. Run this
#   $ nsml run  07-data_read.py -i -d diabetes
if 'NSML_DATASET_PATH' in os.environ:  # Check if the path is set
    DATASET_PATH = os.environ['NSML_DATASET_PATH']
    DATASET_NAME = os.environ['NSML_DATASET_NAME']

    print(DATASET_NAME, "in", DATASET_PATH)
    xy = np.loadtxt(os.path.join(DATASET_PATH, 'diabetes.csv'),
                    delimiter=',', dtype=np.float32)
    print(xy)
else:
    print('DATASET_PATH is not set')
