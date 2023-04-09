import pandas as pd
import jieba.posseg
df=pd.read_excel('data.xlsx')
texts=df['texts'].values.tolist()
labels=df['labels'].values.tolist()

i=0
while i<len(labels):
    words=[]
    for w,flag in jieba.posseg.cut(texts[i]):
        if flag=='eng':
            continue
        words.append(w)
    texts[i]=''.join(words)
    i=i+1

i=0
while i<len(labels):
    if labels[i]=='改写':
        labels[i]='AI写作'
    i=i+1
strdata=''.join(texts)
wordset=set(list(strdata))
fc=open('data/cnews/vocab.txt','w+',encoding='utf-8')
fc.write('<PAD>'+'\n')
for word in wordset:
    fc.write(word+'\n')

f1=open('data/cnews/train.txt','w+',encoding='utf-8')
f2=open('data/cnews/test.txt','w+',encoding='utf-8')
f3=open('data/cnews/val.txt','w+',encoding='utf-8')

i=0
while i<len(labels)/2:


    if i%5==1:

        temp=labels[i]+'\t'+texts[i].replace('\n',' ').replace('\t',' ')+'\n'

        f2.write(temp)
        temp = labels[0-i] + '\t' + texts[0-i].replace('\n', ' ').replace('\t', ' ') + '\n'
        f2.write(temp)
    elif i%5==2:
        temp=labels[i]+'\t'+texts[i].replace('\n',' ').replace('\t',' ')+'\n'
        f3.write(temp)
        temp = labels[0-i] + '\t' + texts[0-i].replace('\n', ' ').replace('\t', ' ') + '\n'
        f3.write(temp)
    else:
            temp = labels[i] + '\t' + texts[i].replace('\n', ' ').replace('\t', ' ') + '\n'
            f1.write(temp)
            temp = labels[0 - i] + '\t' + texts[0 - i].replace('\n', ' ').replace('\t', ' ') + '\n'
            f1.write(temp)
    i=i+1