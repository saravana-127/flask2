#! /usr/bin/python

import sys 
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/applicat')

from applicat import app as application
application.secret_key="neeyo09876543" 


