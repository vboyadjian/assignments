#!/usr/bin/env python3
#this script reads from STDIN and greets the person whose name it gets passed in.
import sys
name = sys.stdin.read()
print("Hello " + name + "!")
