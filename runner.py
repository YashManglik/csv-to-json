InputFile= input("Enter the file path:")
with open(InputFile, mode='r') as text:
    InputString = text.read()
    list1 = InputString.split("\n")
    list2 = []
    for i in list1:
        list2.append(i.split(","))
    keys = []
    for i in list2[0]:
        keys.append(i)
    list2.pop(0)
    outputstring = "["
    endstring = ""
    a=len(list2)
    for j in list2:
        x = len(j)
        outputstring += "{"
        for k in range(0, x, 1):
            tempstring = "\"" + keys[k] + "\"" + ':' + "\"" + j[k] + "\""
            outputstring += tempstring
        for l in range(0,a,1):
            if l <= a-1:
                endstring = '},'
                break
            else:
                endstring = '}'
                break
        outputstring += endstring
    outputstring += "]"
    print(outputstring)
with open('test.json', mode='w') as JsonText:
    JsonText.write(outputstring)
