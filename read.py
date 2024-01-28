def checkVulns(banner):
    f = open("valn_banners.txt", "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable: " + banner.strip("\n"))