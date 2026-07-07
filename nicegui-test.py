#imports ui
from nicegui import ui
import re

def regexFind(bannedWords, prop):
    foundWords = []
    parseProp = prop
    for word in bannedWords:
        word = word.lower()
        findWord = r"\b" + word + r"\b"
        matches = re.findall(findWord, parseProp, re.IGNORECASE)
        if len(matches) > 0:
            foundWords.append((word, len(matches)))
            parseProp = re.sub(findWord, "<c>" + word + "</c>", parseProp)
    return foundWords, parseProp

def getData():
    #opens file that the list of "banned words" is currently in
    bannedFile = open('bannedWords.txt', 'r')
    bannedWords = []

    #copies file to a list
    for line in bannedFile:
        line = line.strip()
        line = line.lower()
        bannedWords.append(line)

    #closes file
    bannedFile.close()

    #returns list of "banned words"
    return bannedWords
'''
def altFindWords(bannedWords, prop):

    foundWords = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']    
    parseProp = simplifyString(prop)
    lastChecked = False
    i = 0
    j = parseProp.find(' ')
    while i < len(parseProp) and j != -1:
        word = parseProp[i:j]
        if word in bannedWords:
            wordFound = False
            for k in range(len(foundWords)):
                if foundWords[k][0] == word:
                    wordFound = True
                    foundWords[k][1] += 1
            if wordFound == False:
                foundWords.append([word, 1])
            parseProp = parseProp[0:i] + boldWord(word) + parseProp[j:len(parseProp)]
            j += 7
    
        i = j+1
        while i < len(parseProp) and parseProp[i] not in alpha:
            i += 1
        j = parseProp.find(' ', i)
        if j == -1 and lastChecked == False:
            j = len(parseProp)
            lastChecked = True

    return foundWords, parseProp

def boldWord(word):
    return "<c>" + word + "</c>"

'''

def simplifyString(s):
    newString = s.lower()
    validChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', '-']

    for i in range(len(newString)-1):
        if newString[i] not in validChars:
            newString = newString[0:i] + ' ' + newString[i+1:len(newString)]

    return newString



#altFindWords(getData(), 'Hello World! This is a gay gay homosexual gay test.')

'''
def findBannedWords(bannedWords, prop):
    #capitalizes all words in the users research proposal
    lowerProp = prop.lower()

    #makes a copy of the proposal
    parseProp = prop

    #initializes list of words flagged in the proposal
    flaggedWords = []

    #searches for each item in the "banned words" list
    for word in bannedWords:

        #capitalizes term
        word = word.lower()

        #checks to see if the term has an 'and' operator
        if '&' in word:
            word1, word2 = word.split('&')

            #finds if each term is in proposal
            i1 = lowerProp.find(word1)
            i2 = lowerProp.find(word2)

            #adds flagged term to the flaggedWords list
            #and capitalizes the term(s) in the proposal
            if i1 != -1 and i2 != -1:
                parseProp, count1 = findAll(parseProp, word1, i1)
                parseProp, count2 = findAll(parseProp, word2, i2)
                flaggedWords.append((word1, count1))
                flaggedWords.append((word2, count2))
        elif '+' in word:
            temp = word.strip('+')
            i = lowerProp.find(temp)
            if i != -1:
                parseProp, count = specFind(parseProp, temp, i)
                if count > 0:
                    flaggedWords.append((temp, count))
        else:
            i = lowerProp.find(word)
            if i != -1:
                parseProp, count = findAll(parseProp, word, i)
                flaggedWords.append((word, count))

    #returns the list of flagged terms
    #and the proposal with all flagged terms capitalized
    return flaggedWords, parseProp


endCharacters = [' ', ',', '.', '?', '!', '(', ')', '[', ']', '/', '"', '<', '>', '=', '-', '+', '&', ':', ';', '_', '*', '—']


def specFind(prop, toFind, i):
    parseProp = prop
    upperProp = prop.upper()
    x = 0

    while i != -1:
        start = upperProp[i-1:i]
        end = upperProp[i+len(toFind):i+len(toFind)+1]
        if start in endCharacters and end in endCharacters:
            x += 1
            parseProp = boldSub(parseProp, i, i+len(toFind))
        #erases documented instances of toFind temporarily
        upperProp = fillNothing(upperProp, i+len(toFind))
        #next instance of toFind
        i = upperProp.find(toFind)
    return parseProp, x
    

def boldSub(full, start, end):
    temp = full[start:end]
    while full[start:start+1] not in endCharacters and start > 0:
        start -=1
    if start > 0:
        start += 1
    while full[end:end+1] not in endCharacters and end < len(full):
        end += 1

    beginning = full[0:start]
    ending = full[end:len(full)]
    middle = full[start:end]
    #print(temp + ": " + middle)


    #capitalizes term at full[start:end]
    middle = "<c>" + middle + "</c>"
    new = beginning + middle + ending

    #returns full string with capitalized substring
    return new



def findAll(prop, toFind, i):

    parseProp = prop
    upperProp = prop.upper()
    x = 0

    #loops until there are no more instances of toFind in the proposal
    while i != -1:

        if toFind in upperProp[i:i+len(toFind)].upper():

            x += 1

            #capitalizes toFind
            parseProp = boldSub(parseProp, i, i+len(toFind))

        #erases documented instances of toFind temporarily
        upperProp = fillNothing(upperProp, i+len(toFind))
        #next instance of toFind
        i = upperProp.find(toFind)

    #returns proposal with all instances of toFind capitalized
    return parseProp, x


def fillNothing(fill, end):
    parseProp = ''
    for i in range(end+7):
        parseProp = parseProp + '-'
    parseProp = parseProp + fill[end:len(fill)]
    return parseProp


def save_prop(prop):
    prop = str(prop)
    flaggedWords, prop = findBannedWords(getData(), prop)
    textbox_I.value = prop
    flaggedWords.sort(key=lambda col: col[0])
    flaggedWords.sort(key=lambda col: col[1], reverse=True)
    if len(flaggedWords) > 0:
        for i in range(len(flaggedWords)):
            text = '' + flaggedWords[i][0] + " (" + str(flaggedWords[i][1]) + ")"
            x = ui.button(text, on_click=lambda: scroller.scroll_to(pixels=1194.5)).props('flat unelevated color-none')
            x.move(card)
    else:
        y = ui.label("No words flagged.")
        y.move(card)

'''

def sortAndFormat(flaggedWords):
    flaggedWords.sort(key=lambda col: col[0])
    flaggedWords.sort(key=lambda col: col[1], reverse=True)
    if len(flaggedWords) > 0:
        for i in range(len(flaggedWords)):
            text = '' + flaggedWords[i][0] + " (" + str(flaggedWords[i][1]) + ")"
            x = ui.button(text, on_click=lambda: scroller.scroll_to(pixels=1194.5)).props('flat unelevated color-none')
            x.move(card)
    else:
        y = ui.label("No words flagged.")
        y.move(card)

def mainStuff(prop):
    prop = str(prop)
    flaggedWords, parseProp = regexFind(getData(), prop)
    sortAndFormat(flaggedWords)
    print(parseProp)
    return flaggedWords, parseProp


def inClick():
    if switch.disable():
        switch.enable()
    card.clear()
    switch.value = 'View Mode'
    flaggedWords, parseProp = mainStuff(textbox_I.value)
    display.set_content(parseProp)
    textbox_I.visible = False
    output.visible = True

def showEdit():
    output.visible = False
    textbox_I.visible = True

def showRevision():
    output.visible = True
    textbox_I.visible = False

def switchEm():
    if textbox_I.visible == True:
        output.visible = True
        textbox_I.visible = False
    else:
        output.visible = False
        textbox_I.visible = True

ui.add_body_html('''
    <style type="text/tailwindcss">
        c {
            font-weight: bold;
            color: red;
            text-decoration: none;
        }
    </style>
''')

def modStrip(string):
    formatting = ['<b>', '</b>', '<i>', '</i>', '<u>', '</u>', '<strike>', '</strike>']
    for f in formatting:
        i = string.find(f)
        while i != -1:
            string = string[0:i] + string[i+len(f):len(string)]
            i = string.find(f)
    return string

with ui.row(wrap=True):
    with ui.column():
        scroller = ui.scroll_area().classes('size-128 border')
        with scroller:
            textbox_I = ui.editor(placeholder='Proposal').classes("width-120px").props('autogrow')
            textbox_I._props.update(toolbar=[
                ['left', 'center', 'right', 'justify'],
                ['bold', 'italic', 'underline', 'strike'],
            ])
            output = ui.element('div').classes('size-120')
            with output:
                display = ui.html('<c>Blank proposal</c>').classes('nicegui-editor')
            output.visible = False
        with ui.row(align_items='stretch'):
            switch = ui.toggle(['Edit Mode', 'View Mode'], on_change=lambda e: switchEm())
            switch.disable()
            testbutton = ui.button('Test Proposal', icon='check', on_click=lambda: inClick()).props(f'color={"negative"}')
    cardScroll = ui.scroll_area().classes('w-80 h-128')
    with cardScroll:
        card = ui.card(align_items='start')
ui.run()
