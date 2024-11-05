from fpdf import FPDF
def main():

    name = input("Name:")
    if name:
        try:
            pdf = FPDF(orientation="portrait", format="A4") # tamanho certo
            pdf.add_page() # ok
            pdf.set_font("Times", size=50) # ok
            pdf.cell(0, 40, txt=f"CS50 Shirtificate", align="C")  # tá alinhado
            pdf.image("./shirtificate.png", w=190, h=190, x=10, y=65) # centrada e do tamanho certo


            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Times", size=30)
            pdf.cell(-180, 230, txt=f"{name} took CS50", align="C")
            pdf.output("shirtificate.pdf")
        except:
            print("Invalid Input")


if __name__ == '__main__':
    main()