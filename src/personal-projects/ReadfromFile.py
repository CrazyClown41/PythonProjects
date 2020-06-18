def readFile():
    with open('file_to_read.txt', 'r') as open_file:
        all_text = open_file.read()
        return all_text

def addToDic(all_text):
    name_dict = {}
    for i in all_text:
        name_dict.append(i)
    return name_dict

def countDic(name_dict):
    name_dict.count()

def printDic(name_dict):
    print(name_dict)
