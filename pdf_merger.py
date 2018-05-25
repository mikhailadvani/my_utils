#!/usr/bin/env python
import sys
import argparse
import os
from PyPDF2 import PdfFileMerger

def get_input_pdfs(pdf_folder, pdf_files, reverse):
    if pdf_files is not None:
        return pdf_files
    elif pdf_folder is not None:
        all_files = os.listdir(pdf_folder)
        pdf_files = sorted(filter(lambda file: file.lower().endswith(".pdf"), all_files), reverse=reverse)
        return map(lambda file: os.path.join(pdf_folder, file), pdf_files)
    else:
        print "Need one of input-pdfs or folder"
        exit(1)

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-o','--output-pdf', type=str, help='Output PDFs', required=True)
    arg_parser.add_argument('-i','--input-pdfs', nargs='+', help='Input PDFs')
    arg_parser.add_argument('-f','--folder',type=str,help='Input PDFs folder')
    arg_parser.add_argument("-r", "--reverse", help="Reverse sort", action="store_true")

    args = arg_parser.parse_args()
    return get_input_pdfs(args.folder, args.input_pdfs, args.reverse), args.output_pdf

def merge(input_pdfs, output_pdf):
    merger = PdfFileMerger()
    for pdf in input_pdfs:
        merger.append(open(pdf, 'rb'))

    with open(output_pdf, 'wb') as fout:
        merger.write(fout)


def main():
    input_pdfs, output_pdf = parse_args()
    merger = PdfFileMerger()
    merge(input_pdfs, output_pdf)

if __name__ == "__main__":
    main()
