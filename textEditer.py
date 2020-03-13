def wbcjg(x):#文本初加工
    with open(x) as file_object:
        contents=file_object.read()
    import string
    remove1=contents.maketrans('','',string.punctuation)
    contents=contents.translate(remove1)
    contents=contents.lower()
    contents = list(contents.split())
    return contents
def wbcbcl(x):#文本初步处理，去掉停用词，形成列表
    value =x
    from nltk.corpus import stopwords
    for i in stopwords.words('english'):
        n=value.count(i)
        for j in range(n):
            value.remove(i)
    return value