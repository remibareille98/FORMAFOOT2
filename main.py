import os

from certificat.certificat_pdf import CertificatPDF
from certificat.utils import import_from_json

data = import_from_json(os.path.abspath("ressources/api object/api.json"))

certificat_pdf = CertificatPDF(data=data, orientation="L")

certificat_pdf.make_pdf()
