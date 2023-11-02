"""reading from url and creating a list with the words"""
    #url = 'http://sixty-north.com/c/t.txt'
import sys #to get url as an cmd argument
from urllib.request import urlopen


"""read the text from the http and append in the list"""
def fetch_words(url):      
    story = urlopen(url)

    words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            words.append(word)

    story.close()
    return words


"""print the list"""
def print_item(items):
    for item in items:
        print (item)


"""defined so it can be imported when it is runed as program
to initiate the program because when it is imported as module can't be run"""
def main(url):
    list_words = fetch_words(url)
    print_item(list_words)

if __name__ == '__main__':
    main(sys.argv[1]) #0th argument is the filename

