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

    # def _get_justification_length(self, string: str, width: int):
    #     string_list = string.split()
    #     last_valid_length = 0
    #     for i, mot in enumerate(string_list):
    #         if i == 0:
    #             current_string = mot
    #         else:
    #             current_string += f" {mot}"
    #         length_text = self.get_string_width(current_string)
    #         if length_text < width:
    #             last_valid_length = length_text
    #             continue
    #         else:
    #             return width - last_valid_length
    #     return width - last_valid_length

    def _get_justification_length(self, string: str, width: int):
        words = string.split()
        lengths = []
        cumulative_length = 0

        for word in words:
            word_length = self.get_string_width(word)
            # Ajouter la longueur du mot et d'un espace
            cumulative_length += word_length + 1
            lengths.append(cumulative_length)

        # Retirer la longueur supplémentaire ajoutée après le dernier mot
        if lengths:
            lengths[-1] -= 1
        print(lengths)
        justification_width = 0
        numero_ligne = 1
        for i, length in enumerate(lengths):
            if length < (width * numero_ligne):
                continue
            else:
                justification_width += width * numero_ligne - lengths[i - 1]
                numero_ligne += 1

        print(justification_width)
        return justification_width

    def get_space_text(self, length):
        text = ""
        while self.get_string_width(text) < length:
            text += " "
        return text

    def _add_text(self):
        # Texte avant titre
        texte_avant_titre = f"La société Formafoot certifie que {self.certificat.name} a validé avec succès la formation:"
        font_size = 14
        self.set_font("Graebenbach-Regular", "", font_size)
        self.set_xy(105, 135)
        self.multi_cell(w=150, h=6, text=texte_avant_titre)
        # Titre
        length_text_avant_titre = self.get_string_width(texte_avant_titre)
        justification_length = self._get_justification_length(
            texte_avant_titre,
            150,
        )
        length_totale = length_text_avant_titre + justification_length
        self.set_font("Graebenbach-Bold", "", font_size)
        text_titre = self.get_space_text(length_totale)
        text_titre += f"«{self.certificat.titre}»"
        self.set_xy(105, 135)
        self.multi_cell(
            w=150,
            h=6,
            text=text_titre,
        )

        length_text_avec_titre = self.get_string_width(text_titre)
        justification_length_titre = self._get_justification_length(
            text_titre,
            150,
        )
        length_totale_avec_titre = length_text_avec_titre + justification_length_titre
        text_session = self.get_space_text(length_totale_avec_titre)
        text_session += f"lors de la session de {self.certificat.month_date}."
        self.set_font("Graebenbach-Regular", "", font_size)
        self.set_xy(105, 135)
        self.multi_cell(w=150, h=6, text=text_session)

    def _add_nom_formatteur(self):
        self.set_font("Graebenbach-Bold", "", 14)
        self.set_xy(105, 163)
        self.cell(text=f"Fabien Richard")
        self.set_font("Graebenbach-Regular", "", 10)
        self.set_xy(105, 169)
        self.cell(text=f"Préparateur physique")
        self.set_xy(105, 173)
        self.cell(text=f"Instructeur FIFA")

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
