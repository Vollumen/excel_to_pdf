import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# Create list to store multiple filepaths
filepaths = glob.glob('text_files/*.txt')

# Create ONE pdf file (put outside loop)
pdf = FPDF(orientation='P', unit='mm', format='A4')

# For loop: Read all fies and create dataframes in python    
# Print page in pdf for each iteration
# Extract content form text files on each iteration

for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf.add_page()
    filename = Path(filepath).stem
    heading = filename.split('.')[0]
    heading = heading.title()
    pdf.set_font(family='Times', size=22, style='B')
    pdf.cell(w=50, h=10, txt=(heading), ln=1)
pdf.output('output.pdf')