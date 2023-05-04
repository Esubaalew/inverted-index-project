
from ntpath import join
from pydoc import doc
from turtle import goto
from unicodedata import name
from webbrowser import open_new
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd


nltk.download()  # can load nltk to machine comment if already


def tokenizer(textToBeTokenized):
    tokenizedText = nltk.word_tokenize(textToBeTokenized)
    tokenizedTextWithNoChars = [
        word.lower() for word in tokenizedText if word.isalpha()]
    tokenizedTextWithNoChars.sort()
    # print("After numbers and special chars removed")
    # print(tokenizedTextWithNoChars)
    return tokenizedTextWithNoChars


def stopWordRemover(tokenizedtext):  # this function will take tokenized
    # text as an argument
    from nltk.corpus import stopwords
    set(stopwords.words('english'))
    print()

    text_NO_SW = [
        word for word in tokenizedtext if not word in stopwords.words()]
    # print("TEXT WITH STOPWORDS REMOVED")
    # print(text_NO_SW)
    return text_NO_SW


def stemmer(nonStopwordText):
    # this function takes text returned by
    # stopWordRemover()
    porter = PorterStemmer()
    stemmed = [porter.stem(each_token)
               for each_token in nonStopwordText]
    return stemmed


def TF(stemmdWord):

    return pd.value_counts(np.array(stemmdWord))


def members():
    member = '''

   BEHINDE THIS CODE ARE THE FOLLOWING PERSONALITIESS

   Azeb Mihiretie\n
   Esubalew Chekol \n
   Hayat Ebrahim \n
   Lidiya Fikrie \n 
   Bereket Gebeyaw \n 
   '''
    print(member)


# mainmmethod
while True:

    main = int(input(
        "Enter 1 if you want to start with string input or 2 if you want with file\n"))
    if main == 1:
        get = input("Enter the text \n")
        print("got it")
        print("Use the following keys to start...")
        print("................................................")
        print(" \
        1. to tokenize \n \
        2. to remove stopword \n\
         3. to stem \n\
         4. to generate indexed vocabulary \n                                        ")
        print(".....................................................")
        user = int(input("What do you need? \n"))

        if user == 1:
            print("THE TOKENIZED, WITH NO PUCTUATUION AND NUMBER \n \
                WITH ALPHABETICAL ORDER ")
            print("------------------------------------------------------")
            tokens = tokenizer(get)
            print(tokens)
            print("------------------------------------------------------")
        elif user == 2:
            print(" TOKENS WITH NO STOP WORD ")
            print("------------------------------------------------------")
            tokens = tokenizer(get)
            NoSW = stopWordRemover(tokens)
            print(NoSW)
            print("------------------------------------------------------")
        elif user == 3:
            print(" STEMMED TOKENS ")
            print("------------------------------------------------------")
            tokens = tokenizer(get)
            NoSW = stopWordRemover(tokens)
            stemmed = stemmer(NoSW)
            print(stemmed)
            print("------------------------------------------------------")

        elif user == 4:
            print("inverted index")

            # 1.tokenize and puctuation and number removal and sorting alphabetically
            tokenized = tokenizer(get)

            # 2 stopwords removal

            with_no_stopword = stopWordRemover(tokenized)

            # print(with_no_stopword)

            # step 3 stemming
            print("---------------------------------------------------------------")
            print("WORD           TF")
            print("---------------------------------------------------------------")
            stemmed = stemmer(with_no_stopword)

            # step 4 calculate TF and rank using number of occurence
            results = TF(stemmed)
            print(results)
        else:
            print("SORRY!", user,
                  " is not defined key , \n I only understand 1,2,3 and 4 ")

    elif main == 2:
        print("you entered ", 2,
              " so I will process the file based on the path mentioned-\n \
            from the code writers machine.\n \
            you can get the the the path of the text1, text2..\n \
            paths to your computer(These are samples our group tried to provide)\
           \n or give the valid path of any txt from your PC  ")
        print("===========================================================")

        path = "C:\\Users\\esuba\\OneDrive\\Documents\\IRPY\\Docs\\text1.txt"
        fil = open(path)
        file = fil.read()
        print("Use the following keys to start...")
        print(".....................................................")
        print(" \
        1. to tokenize \n \
        2. to remove stopword \n\
         3. to stem \n\
         4. to generate indexed vocabulary \n                                        ")
        print(".....................................................")
        user = int(input("What do you need? \n"))

        if user == 1:
            print("THE TOKENIZED, WITH NO PUCTUATUION AND NUMBER \n \
                WITH ALPHABETICAL ORDER ")

            print("------------------------------------------------------")
            tokens = tokenizer(file)
            print(tokens)
            print("------------------------------------------------------")
        elif user == 2:
            print(" TOKENS WITH NO STOP WORD ")
            print("------------------------------------------------------")
            tokens = tokenizer(file)
            NoSW = stopWordRemover(tokens)
            print(NoSW)
            print("------------------------------------------------------")
        elif user == 3:
            print(" STEMMED TOKENS ")
            print("------------------------------------------------------")
            tokens = tokenizer(file)
            NoSW = stopWordRemover(tokens)
            stemmed = stemmer(NoSW)
            print(stemmed)
            print("------------------------------------------------------")

        elif user == 4:
            print("inverted index")

            # 1.tokenize and puctuation and number removal and sorting alphabetically
            tokenized = tokenizer(file)

            # 2 stopwords removal

            print("--------------------------------------------------------")
            with_no_stopword = stopWordRemover(tokenized)

            # print(with_no_stopword)

            # step 3 stemming
            print("WORD           TF")
            print("---------------------------------------------------------------")
            stemmed = stemmer(with_no_stopword)

            # step 4 calculate TF and rank using number of occurence
            results = TF(stemmed)
            print(results)
        else:
            print("SORRY!", user,
                  " is not defined key , \n I only understand 1,2,3 and 4 ")

    if (input("Do you want to continue,  y/n? ")) == "n":
        members()
        print("GOOD BYE, THANK YOU!")
        print("--------------------------------------")
        break
