from fpdf import FPDF

DATA = (
    ("First name", "Last name", "Age", "City"),
    ("Lucas", "Cimon", "31", "Saint-        -sur-Loire"),
)
COL_WIDTHS = (0.2, 0.2, 0.15, 0.45)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier", size=10)  # this trick is easier with monospaced fonts
line_height = pdf.font_size * 2.5
for row in DATA:
    for i, datum in enumerate(row):
        col_width = COL_WIDTHS[i] * pdf.epw
        x, y = pdf.x, pdf.y
        pdf.multi_cell(col_width, line_height, datum, border=1, ln=3)
        if datum.endswith("sur-Loire"):  # performing a 2nd pass on the target cell
            text = "      Mathurin"  # part of cell context to put in bold, with padding matching the word horizontal position
            pdf.set_xy(x, y)  # positioning FPDF to re-draw the same cell
            pdf.set_font(style="BI")  # switching to bold italic
            pdf.multi_cell(col_width, line_height, text, border=1, ln=3)
            pdf.set_font(style="")  # switching back to regular
    pdf.ln(line_height)
pdf.output("issue_108.pdf")
