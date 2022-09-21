from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(csv_path, report_type):
        with open(csv_path) as file:
            csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
            csv_list = list(csv_file)
            
            if report_type == "simples":
                return SimpleReport.generate(csv_list)
            else:
                return CompleteReport.generate(csv_list)
