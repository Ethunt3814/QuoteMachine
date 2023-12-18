import json

#change discord name to reporters name
def reporterNickName(reporter):
    match reporter:
        case "discord nickname":
            return "Name of reporter"
    return

quotes = []

content = ""
reporter = ""
date = ""
name = ""
f = open("quotes.txt", "r", encoding='utf-8')
lines = len(f.readlines())
f.seek(0)


#loops through lines of quotes.txt 
i=0
while i < lines:
    line = f.readline()
    i+=1
    if " — " in line:
        reporter = line.partition(" — ")[0]
        reporter = reporterNickName(reporter)
        date = line.partition(" — ")[2]
        date = date[:-1]
    else:
        line = f.readline()
        i+=1
        continue

    line = f.readline()
    i += 1
    
    if line[0] == '"':
        x = line.rfind('"')
        content = line[1:x]
        name = line[x+2:-1]
        if name == "":
            name = f.readline()[:-1]
            i+=1
        if name != "":
            while name[0] == ' ' or name[0] == '-':
                name = name[1:]

    quote = {'content': content, 'reporter': reporter, 'date': date, 'name':name}

    quotes.append(quote)
f.close()

#make quotes into usable json format
quotesJson = ""

for i in quotes:
    quotesJson = quotesJson + json.dumps(i) + ","
quotesJson = "[" + quotesJson[:-1] + "]"

f = open("sortedQuotes.json", "a")
f.write(quotesJson)
f.close()