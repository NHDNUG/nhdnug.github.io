import codecs
import xml.etree.ElementTree as etree

tree = etree.parse('speakers.xml')
root = tree.getroot()
print(root)

outputpath = 'Z:\\_speakers\\drafts\\'
filename = None
title = None
twitter = None
www = None
email = None
pagecontent = None


for speaker in root:
    # We're looking at the individual speakers now.
    for child in speaker:
        # This is the properties of each speaker:
        # Email, Phone, Name, etc.
        if child.tag == 'filename':
            filename = child.text
        if child.tag == 'title':
            title = child.tag + ': \"' + child.text + '\"'
        if child.tag == 'twitter':
            if child.text is not None:
                twitter = child.tag + ': \"https://twitter.com/' + child.text + '\"'
            else:
                twitter = None
        if child.tag == 'www':
            if child.text is not None:
                www = child.tag + ': \"' + child.text + '\"'
            else:
                www = None
        if child.tag == 'email':
            if child.text is not None:
                email = child.tag + ': \"' + child.text + '\"'
            else:
                email = None
        if child.tag == 'pagecontent':
            if child.text is not None:
                content = child.text.encode("utf8")
                pagecontent = content
            else:
                pagecontent = None
    # Once all of the tags are set, we can write the speaker to the md file.
    print (filename)
    targetpath = outputpath + filename
    target = open(targetpath, 'w')
    target.truncate()
    target.write('---')
    target.write('\n')
    target.write(title)
    target.write('\n')
    target.write("social: ")
    target.write('\n')
    if twitter is not None:
        target.write("    {}".format(twitter))
        target.write('\n')
    if www is not None:
        target.write("    {}".format(www))
        target.write('\n')
    if email is not None:
        target.write("    {}".format(email))
        target.write('\n')
    target.write('---')
    if pagecontent is not None:
        target.write('\n')
        target.write(pagecontent)
        target.write('\n')
        target.write('<!--more-->')
        target.write('\n')
        target.write('<!--excerpt-->')
    else:
        target.write('\n')
        target.write('No bio provided.')
    target.write('\n')
    target.close()


# ---
# title: "Greg Major"
# image-sm: "/images/speakers/greg-major.jpg"
# social:
#     github: "https://github.com/gregmajor"
#     facebook: "https://www.facebook.com/greg.major"
#     linkedin: "https://www.linkedin.com/in/gregmajor"
#     twitter: "https://twitter.com/gregmajor"
#     www: "http://www.gregmajor.com"
# ---
#
# I'm a polyglot software architect, husband, father, woodworker,
# homebrewer, amateur radio operator (KD0FEP), guitar player, runner,
# and cyclist. I've lived in Stillwater, OK, Corpus Christi, TX, Houston,
# TX, Caribou, ME, Minneapolis, MN, and now I call Houston home sweet home.
# <!--more-->
# <!--excerpt-->
