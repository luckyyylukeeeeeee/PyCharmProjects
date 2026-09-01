from PyPDF2 import PdfMerger

merger = PdfMerger()
for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)
merger.write("output.pdf")
merger.close()
