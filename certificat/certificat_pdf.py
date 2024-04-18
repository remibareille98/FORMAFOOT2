# L'import commence par un "." parce que nous sommes dans un package.
import os

from fpdf import FPDF

from .certificat import Certificat


class CertificatPDF(FPDF):
    def __init__(
        self,
        data,
        orientation="L",
    ):
        super().__init__(orientation)
        self.certificat = Certificat(data)

    def _add_image_background(self):
        self.image(
            os.path.abspath("ressources/exemple design/fond-certificat.png"),
            x=0,
            y=0,
            h=self.h,
            w=self.w,
        )

    def _add_date(self):
        self.set_font("Graebenbach-Regular", "", 10)
        self.set_xy(105, 62)
        self.cell(text=f"Fait le {self.certificat.full_formated_date}")

    def _add_text(self):
        self.set_font("Graebenbach-Regular", "", 14)
        self.set_xy(105, 135)
        self.multi_cell(
            w=150,
            text=f"La société Formafoot certifie que {self.certificat.name} a validé avec succès la formation {self.certificat.titre} lors de la session de {self.certificat.month_date}.",
        )

    def _add_nom_formatteur(self):
        self.set_font("Graebenbach-Bold", "", 14)
        self.set_xy(105, 163)
        self.cell(text=f"Fabien Richard")
        self.set_font("Graebenbach-Regular", "", 10)
        self.set_xy(105, 168)
        self.cell(text=f"Préparateur physique")

    def make_pdf(self):
        self.add_page()
        self.add_font(
            "Graebenbach-Regular",
            "",
            os.path.abspath("ressources/fonts/Graebenbach-Regular.otf"),
        )
        self.add_font(
            "Graebenbach-Bold",
            "",
            os.path.abspath("ressources/fonts/Graebenbach-Bold.otf"),
        )
        self.set_text_color(3, 16, 58)
        self._add_image_background()
        self._add_date()
        self._add_text()
        self._add_nom_formatteur()
        self.output("certificat.pdf")
