import re

# print(re.search(r"[A-Z]la", "ala Ola Ela"))
#
# print(re.match(r"[A-Z]la", "ala Ola Ela"))
#
# print(re.fullmatch(r"[A-Z]la", "Ela"))
#
# print(re.findall(r".la", "Ola ala Ela"))
#
# print(re.split(r",|\.|/", ".ap|ple.,pear,gra/pes,carrot.cabbage,veggies.fruit,yard"))
#
# print(re.sub(r"[a-z]{4}", "dog", "Alice has cat"))
#
# print(re.subn(r"[a-z]{4}", "dog", "Alice has cat"))


if __name__ == "__main__":
    text = "Thomas W. (33), last seen in Krakow"
    pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\. \(\d+\))"
    match = re.search(pattern, text)
    print(match)
    print(match.groups())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

    text = "Thomas (33) i Eva (24) agreed to go shopping together tomorrow"
    pattern = r"([A-Z]{1}[a-z]+) \((\d+) l.\)"
    print(re.findall(pattern, text))