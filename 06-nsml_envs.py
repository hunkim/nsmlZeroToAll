"""Environment variables and nsml
==================================

Environment variables are an integral concept of nsml. With them e.g.
information about dataset locations are made accessible to the code. This
example shows how to access environment variables.

"""

import os

# Run nsml with -i (interactive option)
# $ nsml run  06-nsml_envs.py -i

# Print nsml env variables
for key in os.environ.keys():
    print(key, os.environ[key])
