import xml.etree.ElementTree as etree
tree = etree.parse('speakers.xml')
root = tree.getroot()
print(root)

for speaker in root:
    print(speaker.tag, speaker.attrib)
    for child in speaker:
        print(child.tag, child.text)

