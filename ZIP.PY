import zipfile

def extractFIle(zFILE,password):
    try:
        zFILE.extractall(pwd=password)
        return password
    except:
        return
    
def main():
    zFILE=zipfile.ZipFile('evil.zip')
    passFile=open('dictionary.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        guess=extractFIle(zFILE,password)
        if guess:
            print ('[+] Password = '+password+'\n')
            exit(0)

if __name__=='__main__':
    main()