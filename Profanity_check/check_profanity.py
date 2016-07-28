import urllib

def read_text():
    quotes = open(r"E:\GitHub\python\learning-python\Profanity_check\random_text.txt")
    contents_file = quotes.read()
    quotes.close()
    check_profanity(contents_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if output == "true":
        print("Beware of curse words! Profanity Alert!!")
    else:
        print("You're good, no curse words!")
    print(output)
    connection.close()

read_text()
