"""Open a file with correct encoding"""

def predictEncoding(file_path):
    '''Predict a file's encoding using chardet'''
    import chardet
    import os
    encoding = ''
    bytes = min(1024, os.path.getsize(file_path))

    # Open the file as binary data
    raw = open(file_path, 'rb').read(bytes)

    result = chardet.detect(raw)
    encoding = result['encoding']

    return encoding


filename = 'encodingTest.txt'

encoding_str = predictEncoding(filename)
print(encoding_str)

if not encoding_str or encoding_str == 'ISO-8859-1': #  Extended ASCII
    encoding_str = None # as default
    
with open(filename, "r", encoding=encoding_str) as f:
    for line in f:
        print(line)
