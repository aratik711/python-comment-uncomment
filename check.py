import re
import sys
import getopt

def comment(regex):
    with open("sample", 'r+') as f:
        text = f.read()
        text = re.sub(r'^{}'.format(regex), r'#{}'.format(regex), text, flags = re.M)
        f.seek(0)
        f.write(text)
        f.truncate()
def uncomment(regex):
    new_text = ''
    with open("sample", 'r+') as f:
        for text in f:
            text1 = re.findall(r"^#{}".format(regex), text)
            if text1:
                text = re.sub(r'^#', '', text, flags = re.M)
            new_text += text
        f.seek(0)
        f.write(new_text)
        f.truncate()
try:
        options, args = getopt.getopt(
            sys.argv[1:], "c:u:",
            ["comment=", "uncomment="])
        for name, value in options:
            if name in ('-c', '--comment'):
                comment(value)
            if name in ('-u', '--uncomment'):
                uncomment(value)
except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(1) 


