import sys
import os

#hack around absolute paths
#current_dir =  os.path.abspath(os.path.dirname(__file__))
#parent_dir = os.path.abspath(current_dir + "/../")

sys.path.insert(0, "/srv/www/app/")

from apache_flask import app as application