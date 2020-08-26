#! /usr/bin/python

import sys 
import logging
logging.basicConfig(stream=sys.stderr)


from applicat import app as application
application.secret_key="neeyo09876543" 


