# In[1]:

import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# In[2]:
import re
import math
import glob

# In[3]:

#change the path to folder that has the PDF files
path = '/home/shreyansh/pdcda/PDFfiles'
pathlen=len(path)
#to get the path of every pdf in the folder
files = [f for f in glob.glob(path + "**/*.pdf")]

# In[4]:


def convert_pdf_to_txt(path):	
    #given the path of the file as argument, the function reads the pdf and returns the text in it
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)        
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

# In[5]:

def FilterDoc(files):
    #the function extracts words from the txt in pdf and appends in a list
    termsDoc=[]
    names=[]
    for i in files:
        x=convert_pdf_to_txt(i) #receiving the text from the pdf
        x = re.findall('[a-zA-Z]{2}[a-zA-z]*',x) #extratcing the words from text
        termsDoc.append([a.lower() for a in x]) #append the wrords list of the pdf 
        names.append(i[pathlen+1:]) #append the name from the path of the pdf
    return termsDoc, names


# In[6]:

# 'sw' is the list of stop words    
sw=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
tdoc=[]
termsDoc=[]
completeList=[]

# In[7]:

termsDoc,names=FilterDoc(files)
print("\n\nThe Pdfs available are:\n")
s=0
for i in names:
    print(s+1,") ",i)
    s=s+1

# In[8]:

#function to remove the stop words from text of each document
def RemStopWords(termsDoc):
    global sw
    termsDoc1=termsDoc
    for i in range(len(names)):
        termsDoc[i]=[a for a in termsDoc[i] if a not in sw]
    return termsDoc,termsDoc1


# In[9]:
termsDoc,termsDoc1=RemStopWords(termsDoc)


def CreatingList(termsDoc):
    #the function creates a list of words from all the pdfs combined
    global sw
    global completeList
    trial=[]
    #trial=ai+wm+dm
    #print(len(trial),len(ai))
    trial = [a for a in termsDoc]
    for i in trial:
        for j in i:
            if j not in sw:
                completeList.append(j)
    completeList=list(set(completeList))
    #list of unique words from all the pdfs
CreatingList(termsDoc)

# In[11]:


def BooleanMatrix(termsDoc1):
    """the function forms the frequency matrix of document against the words with
    percentage occurance of the word in the document (weightage of the word in that pdf)
    If a words does not exist in the pdf the weightage is zero"""
    global completeList
    lenOfDocs=[]
    for i in termsDoc1:
        lenOfDocs.append(len(i)) #list with length of each doc
    l=-1
    bools=[]
    for k in termsDoc:
        temp=[]
        l=l+1
        for i in completeList:
            if(i in k):
                x=k.count(i) # no. occurances of the word 'i' in the document 'k'
                temp.append(x/lenOfDocs[l]) #converting to percentage
            else:
                temp.append(0)
        bools.append(temp)
    mat=[completeList]
    for i in bools:
        mat.append(i)
    return mat

# In[13]:
    
mat=BooleanMatrix(termsDoc1)


def idfVector(mat):
    """creating the idf vector with idf values of all the words"""
    global completeList
    idf=[]
    for i in range(len(completeList)):
        c=0
        for j in range(len(names)):
            #print(mat[j+1][i])
            if(mat[j+1][i]>0):
                c=c+1
        if(c!=0):
            idfx=math.log((1+3)/c) #formula to calculate the idf
        else:
            idfx=0
        idf.append(idfx)
    return idf


# In[14]:
    
def GetQuery():
    #function to input the query
    query=input("Enter The Query: ").lower().split()
    return query
# In[15]:
    
def QueryDoc(query):
    #converting the query to document to calculate the relevance with the other pdfs
    qmat=[]
    qmat.append(query)
    qmat.append([])
    for i in range(len(qmat[0])):
        qmat[1].append(1)
    s=sum(qmat[1])
    for i in range(len(qmat[0])):
        qmat[1][i]=qmat[1][i]/s
    return qmat
# In[16]:
query=GetQuery()
qmat=QueryDoc(query)
idf=idfVector(mat)

def idfQueryDoc(qmat):
    #filtering the idfs for the words in the query
    idfq=[]
    index=[]
    for j in range(len(qmat[0])):
        for i in range(len(mat[0])):
            if(mat[0][i]==qmat[0][j]):
                index.append(i)
                idfq.append(idf[i])
                break
    return idfq, index

# In[17]:

idfq,index=idfQueryDoc(qmat)

def tfidfQuery(qmat,idfq,idf):
    #multiplying the query document with the idf vector do that the words get their weightage
    for i in range(len(qmat[1])):
        qmat[1][i]=qmat[1][i]*idfq[i]
    return qmat

# In[18]:
qmat=tfidfQuery(qmat,idfq,idf)

def filteredMatrix(mat,qmat,index):
    #filtering the documents that have the words in that are in the query
    mfq=[]
    for i in range(len(mat)):
        mfq.append([])
        for j in range(len(qmat[0])):
            mfq[i].append(mat[i][index[j]])
    return mfq


# In[19]:
mfq=filteredMatrix(mat,qmat,index)

def FinalDict(mfq):
    #finding the ranking of the filtered pdfs based on query
    final={}
    for j in range(1,len(mfq)):
        value=0
        for i in range(len(qmat[0])):
            value=value+mfq[j][i]*qmat[1][i] #clculating the closeness value of the pdf with the query
        if(value!=0):
            final[value]=j
    return final

# In[20]:
final=FinalDict(mfq)

# In[21]:
#sorting the docs based on ranks
def FinalOutput(final):
    x=sorted(final)
    for i in range(len(x)):
        print(i+1,") ",names[final[x[i]]-1])

# In[22]:
print("\n\nThe pdfs selected and ranked for the given query are:\n")
FinalOutput(final)

