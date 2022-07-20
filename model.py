import PyPDF2
import pickle
import os

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity
# model_name = 'multi-qa-MiniLM-L6-cos-v1'
# # sbert = 'bert-base-nli-mean-tokens'
# model = SentenceTransformer(model_name)
def fscore():
    filename = r"C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\finalized_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))

    resume = r"C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\uploads\resume.pdf"
    fileReader = PyPDF2.PdfFileReader(resume)

    # print the number of pages in pdf file
    pageObj = fileReader.getPage(0)

    # extracting text from page
    resume = pageObj.extractText()

    jd = open(r"C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\uploads\jd.txt", "r").read()


    # print('jd is **********************************************************************')
    resume = loaded_model.encode(resume)
    jd = loaded_model.encode(jd)
    score = cosine_similarity([resume], [jd])[0][0]
    dir = r'C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\uploads'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    return int(score*10)


