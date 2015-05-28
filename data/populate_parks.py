import json
import os
import sys


script_path = os.path.dirname(os.path.realpath('__file__'))
project_dir = os.path.abspath(os.path.join(script_path, '..', 'parks'))
sys.path.insert(0, project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'parks.settings'

from parks_geo.models import Park


if __name__ == "__main__":
    with open("parks.json") as j:
        parks = json.loads(j.read())['data']

        for park in parks:
            new_park = Park(name=park[9], feature=park[8], address=park[10],
                            latitude=float(park[12]), longitude=float(park[13]))
            new_park.save()
