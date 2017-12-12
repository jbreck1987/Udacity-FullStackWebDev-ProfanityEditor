import urllib.request


def file_reader(fileLocation):
    FILE = open(fileLocation, 'r')
    return FILE.read()
    FILE.close()


def check_profanity(text):
    http_connection = urllib.request.urlopen(
        'http://www.wdylike.appspot.com/?q={}'.format(text))
    request = http_connection.read()
    http_connection.close()
    return request


uri = input('Please enter the path to the file: ')
textfile = file_reader(uri)
result = str(check_profanity(textfile)).strip('b\'')

if result == 'true':
    print('Your word is a curse word!')
elif result == 'false':
    print('Your word is good to go!')
else:
    print('Sorry, we ran into an error')
