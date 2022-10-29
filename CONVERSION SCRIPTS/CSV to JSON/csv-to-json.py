import csv
import json


def csv_to_json(input_csv: str, output_json: str) -> bool:
    """
     Funtion to Convert csv to json file
     Funtion might need some changes according to your file organization and type
    """

    with open(input_csv, "r") as file_obj:
        reader = list(csv.DictReader(file_obj))
        json_obj = json.dumps(reader)

    with open(output_json, "w") as file_obj:
        file_obj.writelines(json_obj)

    return True
