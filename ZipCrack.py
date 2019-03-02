import zipfile
from optparse import OptionParser
from threading import Thread

def extract(zip, passw):
    try:
        zip.extractall(pwd=passw)
        print '[+] Success! The Password Is:', passw
        return
    except:
        pass

def crackZip(zip, dic):
    print '[*] Trying to crack: ' + zip.filename
    for word in dic.read().splitlines():
        t = Thread(target=extract, args=(zip, word))
        t.start()

    #print '[-] The password couldn\'t be found'

def main():
    #option parse for command line use
    parser = OptionParser("-f <zipfile> -d <dictionary> ")
    parser.add_option("-f", "--file", type="string", dest="zip", help="The ZIP File you want to crack.")
    parser.add_option("-d", "--dictionary", type="string", dest="dict", default="res/10kpasswords.txt", help="The dictionary which is used to crack the ZIP.")
    parser.add_option("-q", "--q", action="store_true", default="false", help="Quiet mode.")
    (options, args) = parser.parse_args() #parse

    if (options.zip == None):
        print parser.usage
        exit(0)
    else:
        dictPath = options.dict
        zipPath = options.zip



    #do stuff
    dict = open(dictPath, 'r')
    zip = zipfile.ZipFile(zipPath)
    crackZip(zip, dict)

if __name__ == '__main__':
    main()