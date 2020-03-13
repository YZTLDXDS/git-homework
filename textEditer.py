def wbcjg(x):#文本初加工
    with open(x) as file_object:
        contents=file_object.read()
    import string
    remove1=contents.maketrans('','',string.punctuation)
    contents=contents.translate(remove1)
    contents=contents.lower()
    contents = list(contents.split())
    return contents
    