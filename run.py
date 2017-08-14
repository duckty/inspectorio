#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: run.py
# Author: Khuong Nguyen <khuong@inspectorio.com>
# Date: 14.08.2017
# Last Modified Date: 14.08.2017
# Last Modified By: Khuong Nguyen <khuong@inspectorio.com>
from flask import Flask
app = Flask(__name__)

@app.route("/api/<name>")
def hello(name):
        return "Hello World {}".format(name)
