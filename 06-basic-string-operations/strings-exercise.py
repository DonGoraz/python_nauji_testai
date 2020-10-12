# sentence = "Lorem ipsum - tai fiktyvus tekstas naudojamas spaudos ir grafinio dizaino pasaulyje jau nuo XVI a. pradžios. Lorem Ipsum tapo standartiniu fiktyviu tekstu, kai nežinomas spaustuvininkas atsitiktine tvarka išdėliojo raides atspaudų prese ir tokiu būdu sukūrė raidžių egzempliorių. Šis tekstas išliko beveik nepasikeitęs ne tik penkis amžius, bet ir įžengė i kopiuterinio grafinio dizaino laikus. Jis išpopuliarėjo XX a. šeštajame dešimtmetyje, kai buvo išleisti Letraset lapai su Lorem Ipsum ištraukomis, o vėliau -leidybinė sistema AldusPageMaker, kurioje buvo ir Lorem Ipsum versija."
# sentence = '0123456789'
# ilgis =len(sentence))
# lyginis =len(sentence) % 2
#
# if lyginis == 0:
#     middle = len(sentence) / 2
#     print(middle)
#     print(sentence[])


testString = '0123456789'
stringLength = len(testString)
if stringLength % 2 == 0:
    middleSubstring = testString[stringLength // 2 - 2: stringLength // 2 + 2]
else:
    middleSubstring = testString[stringLength // 2 - 2: stringLength // 2 + 3]
print(middleSubstring)
