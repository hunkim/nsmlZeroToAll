import os
import numpy as np

# 1. run nsml
#   $ nsml run ...
# 2. download the session
#   $ nsml download <session_id>

with open('nsml_file_save.txt', 'w') as file:
    file.write('Stored after session')
