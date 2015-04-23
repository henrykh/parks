import json

if __name__ == "__main__":
    with open("parks.json") as j:
        parks = json.loads(j.read())
    import pdb; pdb.set_trace()
