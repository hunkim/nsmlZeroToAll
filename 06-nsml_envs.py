import os

# Run nsml with -i (interactive option)
# $ nsml run  06-nsml_envs.py -i

# Print nsml env variables
for key in os.environ.keys():
    print(key, os.environ[key])
