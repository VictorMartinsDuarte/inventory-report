from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def csv(path):
        with open(path) as file:
            return list(csv.DictReader(file))

    def json(path):
        with open(path) as file:
            return json.load(file)

    def xml(path):
        list = []
        xml = ET.parse(path).getroot()
        for item in xml:
            item_dict = {}
            for attribute in item:
                item_dict[attribute.tag] = attribute.text
            list.append(item_dict)
        return list

    @classmethod
    def import_data(cls, file_path, report_type):
        def check_extension(path):
            if path.endswith('.csv'):
                return cls.csv(path)
            elif path.endswith('.json'):
                return cls.json(path)
            else:
                return cls.xml(path)

        if report_type == "simples":
            return SimpleReport.generate(check_extension(file_path))
        else:
            return CompleteReport.generate(check_extension(file_path))
