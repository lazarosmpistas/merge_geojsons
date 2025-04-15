import json
import os

if __name__ == '__main__':
    config = json.load(open('config.json'))
    folder = config["target_folder"]

    new_dict = {"type": "FeatureCollection", "features": []}
    for filename in os.listdir(folder):
        if filename.endswith('.geojson'):
            geojson_dict = json.load(open(os.path.join(folder, filename)))
            for line in geojson_dict['features']:
                line.update({"filename":filename})
            new_dict["features"] += geojson_dict['features']

    output_location = os.path.join(folder, "merged.geojson")
    with open(output_location, "w") as outfile:
        json.dump(new_dict, outfile)