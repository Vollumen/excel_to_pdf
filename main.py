import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path 

# Create list to store multiple filepaths
filepaths = glob.glob('invoices/*.xlsx') # Get everythong with ending xlsx
print(filepaths)

# Read all files and load into python in the form of pandas dataframe
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    # For each iteration: create a pdf document using FPDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()  # Add page to the pdf
    filename = Path(filepath).stem # Extract part of filename using pathlib/Path. Stem: extract name minus extension
    invoice_nr = filename.split('-')[0] # Extracts the first part/item of list/name 
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {invoice_nr}') # Add content to each page
    pdf.output(f'PDFs/{filename}.pdf')  