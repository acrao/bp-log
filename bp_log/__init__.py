import os
import sys

#Add python modules in lib/ to sys.path
app_dir = os.path.dirname(__file__)
lib_dir = os.path.join(os.path.dirname(app_dir), 'lib')
for package in os.listdir(lib_dir):
    sys.path.insert(0,os.path.join(lib_dir, package))

from flask import Flask
import settings

app = Flask(__name__)

#config here
app.config.from_object('bp_log.settings')

#app imports
import bp_log.views