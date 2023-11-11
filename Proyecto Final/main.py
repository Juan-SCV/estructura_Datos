import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix , classification_report
from arbol import Arbol

df = pd.read_csv("Proyecto Final/spam_ham_dataset.csv")

email_subjects = []
email_text = []
def split_subject(text):
    global email_subjects
    global email_text
    subject = ""
    for ch in text:
        if(ch=='\r'):
            break
        subject+=ch
        
    email_subjects.append(subject)
    email_text.append(text.replace(subject,""))

df["text"] = df["text"].str.replace("Subject:","")
df.loc[df["label"] == "ham","label"] = 0
df.loc[df["label"] == "spam","label"] = 1
df["text"].apply(split_subject)
df["subject"] = email_subjects
df["text"] = email_text  

def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df

df = df.drop(df.columns[0], axis=1)
df = df.drop('label_num', axis=1)
df = swap_columns(df, 'label', 'subject')

def clean_text(s): 
    for cs in s:
        if  not cs in string.ascii_letters:
            s = s.replace(cs, ' ')
    return s.rstrip('\r\n')

def remove_short_words(s): 
    wordsList = s.split()
    k_length=2
    resultList = [element for element in wordsList if len(element) > k_length]
    resultString = ' '.join(resultList)
    return resultString

df['text'] = df['text'].apply(lambda x: clean_text(x))
df['text'] = df['text'].apply(lambda x: remove_short_words(x))
df['subject'] = df['subject'].apply(lambda x: clean_text(x))
df['subject'] = df['subject'].apply(lambda x: remove_short_words(x))

df['label']=df['label'].astype(str).astype(int)
X_train, X_test , y_train, y_test = train_test_split(df['text'], df['label'] , test_size=0.3)

Vectorizer = CountVectorizer()
count = Vectorizer.fit_transform(X_train.values)

Spam_detection = DecisionTreeClassifier()
targets = y_train.values
Spam_detection.fit(count, targets)

y_predict = Spam_detection.predict(Vectorizer.transform(X_test))

accuracy_score(y_test, y_predict)

cm = confusion_matrix(y_test,y_predict)
sns.heatmap(cm, annot = True, fmt = 'd')
plt.xlabel('Predicted')
plt.ylabel('Actual')

arbol = Arbol()

for text, label, predicted_label in zip(X_test, y_test, y_predict):
    is_ham = label == 0
    arbol.insert_data(text, label, predicted_label, is_ham)

arbol.inorden()

print(classification_report(y_test , y_predict))