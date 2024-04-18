from datetime import datetime
import locale


class Certificat:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

    def __init__(self, data: dict):
        self.name = self._certified(data)
        self._date = datetime.strptime(data.get("date"), "%d/%m/%Y")
        self.full_formated_date: datetime = self._format_full_date(data)
        self.month_date: datetime = self._format_month_date()
        self.titre = data["formation"]["titre"]

    def _certified(self, data: dict):
        nom = data["user"]["nom"]
        prenom = data["user"]["prenom"]
        return f"{prenom} {nom}"

    def _format_full_date(self, data: dict):
        return self._date.strftime("%d %B %Y")

    def _format_month_date(self):
        return self._date.strftime("%B %Y")
