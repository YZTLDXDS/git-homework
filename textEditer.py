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
def cptj(x):#词频统计
    from nltk import FreqDist
    ciping=FreqDist(x)
    return ciping
def ciyuntu():
    LJ=E1.get()
    import os
    if not os.path.isfile(LJ):
        wenjianbucunzai()
    else:
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        f = open(LJ).read()
        wordcloud = WordCloud(
            background_color="white",  # 设置背景
            width=1500,  # 设置宽度
            height=960,  # 设置高度
            margin=10  # 设置边缘
        ).generate(f)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()
def wenjianbucunzai():#假设文件不存在
        top2=Tk()
        top2.title('文件不存在')
        top2.geometry("300x200")
        def tc2():
            top2.destroy()
        L2= Label(top2, text='【请输入存在的文件名】')
        L2.pack(pady='11m')
        OK1 = Button(top2, text='OK', command=tc2)
        OK1.pack()
        top2.mainloop()
from tkinter import *

