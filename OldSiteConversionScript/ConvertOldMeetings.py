import xml.etree.ElementTree as etree
import datetime

tree = etree.parse('meetings.xml')
root = tree.getroot()
print(root)


outputpath = 'Z:\\_drafts\\'

filename = None
date = None
title = None
pagecontent = None
location = None
speaker = None
sponsor = None
logo = None


for meeting in root:
    # We're looking at the individual meetings now.
    for child in meeting:
        # This is the properties of each meeting:
        if child.tag == 'filename':
            filename = child.text
        if child.tag == 'date':
            date = child.tag + ':               \"' + child.text + '\"'
        if child.tag == 'title':
            title = child.tag + ':              \"' + child.text + '\"'
        if child.tag == 'pagecontent':
            if child.text is not None:
                content = child.text.encode("utf8")
                pagecontent = content
        if child.tag == 'location':
            location = child.tag + ':           \"' + child.text + '\"'
        if child.tag == 'speaker':
            speaker = child.tag + ':            \"' + child.text + '\"'
        if child.tag == 'sponsor':
            sponsor = child.tag + ':            \"\"'
        if child.tag == 'logo':
            if child.text is not None:
                logo = child.tag + ':           \"' + child.text + '\"'

    # Once all of the tags are set, we can write the speaker to the md file.
    print (filename)
    targetpath = outputpath + filename
    target = open(targetpath, 'w')
    target.truncate()
    target.write('---')
    target.write('\n')
    target.write(date)
    target.write('\n')
    target.write(speaker)
    target.write('\n')
    target.write(title)
    target.write('\n')
    target.write('subtitle:           \"\"')
    target.write('\n')
    target.write(location)
    target.write('\n')
    target.write('location-detail:    \"\"')
    target.write('\n')
    target.write(sponsor)
    target.write('\n')
    target.write('description:        \"\"')
    target.write('\n')
    target.write('---')
    if pagecontent is not None:
        target.write('\n')
        target.write(pagecontent)
        target.write('\n')
    else:
        target.write('\n')
        target.write('No details available.')
    target.write('\n')
    target.close()


