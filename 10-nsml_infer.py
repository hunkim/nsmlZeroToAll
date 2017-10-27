import os
import numpy as np
import nsml

from random import randint


def bind_model(model, **kwargs):
    def save(filename, *args):
        # save the model with 'checkpoint' dictionary.
        print("save your model in the file")

    def load(filename, *args):
        # load the model from the file
        print("load your model from the file")

    def infer(input):
        print("input:", input)
        # infer using the loaded model
        # ...
        # return the results
        return randint(0, 9)

    def evaluate():
        pass

    def decode(input):
        print("decode:", input)

    # function in function is just used to divide the namespace.
    nsml.bind(save, load, infer, evaluate, decode)

# Need to remember some state
nsml.save(10)
