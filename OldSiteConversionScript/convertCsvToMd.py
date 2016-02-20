import csv
outputPath = "C:\Development\InfoCraft\nhdnug.github.io\_drafts"
print outputPath

ifile  = open('nhmeetings.csv', "rb")
reader = csv.reader(ifile)
rownum = 0
datePart = None
titlePart = None
date = None
title = None
description =None
location = None
speaker = None
bio = None
speakerurl = None
email = None
twitter = None
sponsor = None
logo = None

for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            if colnum == 0:
                datePart = col
                date =  ('{} : {}'.format(header[colnum], col))
            if colnum == 1:
                titlePart = col
                title = ('{} : {}'.format(header[colnum], col))
            if colnum == 2:
                description = ('{} : {}'.format(header[colnum], col))
            if colnum == 3:
                location = ('{} : {}'.format(header[colnum], col))
            if colnum == 4:
                speaker = ('{} : {}'.format(header[colnum], col))
            if colnum == 5:
                bio = ('{} : {}'.format(header[colnum], col))
            if colnum == 6:
                speakerurl = ('{} : {}'.format(header[colnum], col))
            if colnum == 7:
                email = ('{} : {}'.format(header[colnum], col))
            if colnum == 8:
                twitter = ('{} : {}'.format(header[colnum], col))
            if colnum == 9:
                sponsor = ('{} : {}'.format(header[colnum], col))
            if colnum == 10:
                logo = ('{} : {}'.format(header[colnum], col))
            colnum += 1
        print title
    rownum += 1
ifile.close()
