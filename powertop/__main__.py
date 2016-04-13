import sys
import json
from .decoder import Powertop

if len(sys.argv) == 1:
    time = 1
elif len(sys.argv) == 2:
    try:
        time = int(sys.argv[1])
    except ValueError:
        print('Syntax: python3 -m powertop [time]')
        exit(1)
else:
    print('Syntax: python3 -m powertop [time]')
    exit(1)

measures = Powertop().get_measures(time=time)

print(json.dumps(measures, indent=4))
