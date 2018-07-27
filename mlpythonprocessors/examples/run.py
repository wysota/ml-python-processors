#!/usr/bin/env python3

import sys
from mountainlab_pytools.mlprocessors.registry import registry, register_processor

registry.namespace="example"

import hello_world

registry.register(hello_world.HelloWorld)
registry.register(hello_world.HelloPerson)
registry.register(hello_world.HelloPersonWithOutput)
registry.register(hello_world.Colorize)

registry.register(hello_world.Replace)


if __name__ == "__main__": 
    registry.process(sys.argv)
