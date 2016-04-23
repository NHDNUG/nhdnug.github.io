import csv
import cgi

outputPath = "Z:\\_drafts"
print outputPath

ifile  = open('nhmeetings.csv', "rb")
reader = csv.reader(ifile, dialect='excel')
rownum = 0

outputFile = None
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
pagecontent = None

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
                date = date
                print date
            if colnum == 1:
                titlePart = col.replace(" ","-")
                titlePart = titlePart.replace("-/-", "-")
                titlePart = titlePart.replace(".", "-")
                titlePart = titlePart.replace("?", "")
                titlePart = titlePart.replace(":", "")
                titlePart = titlePart.replace("---", "-")
                titlePart = titlePart.replace(",", "")
                title = ('{} : {}'.format(header[colnum], col))
                outputFile = '{}\\{}-{}.md'.format(outputPath, datePart, titlePart)
                print title
            if colnum == 2:
                description = ('{} : {}'.format(header[colnum], col))
                description = cgi.escape(description)
                description = description[:50]
                pagecontent = col
                pagecontent = cgi.escape(pagecontent)
                print description
            if colnum == 3:
                location = ('{} : {}'.format(header[colnum], col))
                print location
            if colnum == 4:
                speaker = ('{} : {}'.format(header[colnum], col))
            if colnum == 5:
                bio = ('{} : {}'.format(header[colnum], col))
                bio = cgi.escape(bio)
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
        print outputFile
        target = open(outputFile, 'w')
        target.truncate()
        target.write('---')
        target.write('\n')
        target.write(date)
        target.write('\n')
        target.write(title)
        target.write('\n')
        target.write(description)
        target.write('\n')
        target.write(location)
        target.write('\n')
        target.write(speaker)
        target.write('\n')
        target.write(bio)
        target.write('\n')
        target.write(speakerurl)
        target.write('\n')
        target.write(email)
        target.write('\n')
        target.write(twitter)
        target.write('\n')
        target.write(sponsor)
        target.write('\n')
        target.write(logo)
        target.write('\n')
        target.write('---')
        target.write('\n')
        target.write(pagecontent)
        target.write('\n')
        target.close()
    rownum += 1
ifile.close()


# New format should be
# ---
# att: value
# att: value
# att: value
# att: value
# ---