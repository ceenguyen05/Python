# Program Purpose :
# In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2,
#  a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

from fpdf import FPDF

name = input("What is your name? ")
pdf = FPDF(orientation = 'P', format = 'A4')
pdf.add_page()
pdf.set_font("Arial", 'B', 45)
pdf.cell(0, 60, "CS50 shirtificate", 0, 1, 'C')
pdf.image("shirtificate.png" , x = 0 , y = 70)
pdf.set_xy(50, 150)
pdf.set_font("Arial", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(45, 70, f"{name} took CS50")  # Centered name

pdf.output("shirtificate.pdf")
