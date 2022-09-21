from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        today = date.today().strftime("%Y-%m-%d")
        manufact_dates = [item["data_de_fabricacao"] for item in list]
        oldest_manufact_date = min(manufact_dates)
        due_dates = [item["data_de_validade"] for item in list]
        valid_due_dates = []
        for dates in due_dates:
            if dates > today:
                valid_due_dates.append(dates)
        closest_due_date = min(valid_due_dates)
        company_name = [item["nome_da_empresa"] for item in list]
        company_with_more_products = Counter(company_name).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufact_date}\n"
            f"Data de validade mais próxima: {closest_due_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
