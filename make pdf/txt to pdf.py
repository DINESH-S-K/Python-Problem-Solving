from fpdf import FPDF

#create object
pdf= FPDF()

#add a page
pdf.add_page()

#set style and size of font 
pdf.set_font("Arial",size=15)

#create a cell
pdf.cell(200,10,txt="Python is interpreted and high level programming language",ln=1,align='C')

#save pdf
pdf.output("mypdf.pdf")