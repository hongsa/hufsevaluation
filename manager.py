import sys
if "C:\Program Files (x86)\Google\google_appengine" not in sys.path:
    sys.path.append("C:\Program Files (x86)\Google\google_appengine")

from apps import manager

manager.run()