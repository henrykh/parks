import json

if __name__ == "__main__":
    with open("parks.json") as j:
        parks = json.loads(j.read())['data']
        parks_geojson = {"type": "FeatureCollection",
                         "features": []}
        for park in parks:
            park_geojson = {"type": "Feature",
                            "geometry": {"type": "Point",
                                         "coordinates": [float(park[12]), float(park[13])]
                                         },
                            "properties": {
                                "name": park[9],
                                "address": park[10],
                                "type": park[8],
                                "website": park[11][0]
                            }
                            }
            parks_geojson["features"].append(park_geojson)

        with open('parks_geojson.json', 'w') as outfile:
            json.dump(parks_geojson, outfile)
