import sys
if "/usr/local/google_appengine" not in sys.path:
    sys.path.append("/usr/local/google_appengine")

from apps import manager

manager.run()