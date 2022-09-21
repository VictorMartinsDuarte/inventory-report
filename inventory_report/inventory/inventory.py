from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def csv(path):
        with open(path) as file:
            return list(csv.DictReader(file))

    def json(path):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def import_data(cls, file_path, report_type):
        def verify_extension(path):
            if path.endswith('.csv'):
                return cls.csv(path)
            elif path.endswith('.json'):
                return cls.json(path)

        if report_type == "simples":
            return SimpleReport.generate(verify_extension(file_path))
        else:
            return CompleteReport.generate(verify_extension(file_path))
