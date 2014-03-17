#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from flask.testsuite import main
main()
