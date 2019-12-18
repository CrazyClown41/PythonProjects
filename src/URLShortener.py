dictonary = {}
id = 1

#def get_url(self):        
#orginal_url = str(input("Enter URL you want to shorten: "))
#return orginal_url

def readFile():
    f = open("urls.txt", "r")
    txt = (f.read())
    print(txt)
    f.close()

def shorten_url(self, orginal_url):    
    if orginal_url in self.dictonary:
        id = self.dictonary[orginal_url]
        shorten_url = id
    else: 
        self.dictonary[orginal_url] = self.id
        shorten_url = self.id
        self.id =+ 1
    return "python_url_shorten/id/"+str(shorten_url)

readFile()
#shorten_url()