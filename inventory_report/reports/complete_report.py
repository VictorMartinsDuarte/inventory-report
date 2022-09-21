from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)

        comps = Counter(item["nome_da_empresa"] for item in list)
        prod_by_comp = ""
        for comp, qt in comps.items():
            prod_by_comp += (f"- {comp}: {qt}\n")

        return(
          f"{simple_report}\n"
          f"Produtos estocados por empresa:\n"
          f"{prod_by_comp}"
        )
