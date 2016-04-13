import sys
import json
from .decoder import Powertop

if len(sys.argv) == 0:
    time = 1
elif len(sys.argv) == 1:
    time = sys.argv[0]
else:
    print('Syntax: python3 -m powertop [time]')

measures = Powertop().get_measures(time=1)

print(json.dumps(measures, indent=4))
