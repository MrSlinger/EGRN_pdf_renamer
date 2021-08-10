# -*- coding: utf-8 -*-
from lxml import etree
import os, shutil

#directory = r'C:\Users\1'
directory = r'./'
pdf_ext = ".pdf"
for entry in os.scandir(directory):
    if (entry.path.endswith(".xml")
            or entry.path.endswith(".png1")) and entry.is_file():
        filename, file_extension = os.path.splitext(entry.path)
        #print (filename, file_extension)
        #print (entry.path)
        tree = etree.parse(entry.path)
        cad = tree.xpath('/extract_about_property_land/land_record/object/common_data/cad_number')
        print(cad[0].text)
        sourceFile = filename + pdf_ext
        #destinationFile = cad[0].text + pdf_ext
        destinationFile = os.path.join('./', cad[0].text + pdf_ext).replace(':', '_')
        print (sourceFile, "=>", destinationFile)
        shutil.copy(sourceFile, destinationFile, follow_symlinks=True)
