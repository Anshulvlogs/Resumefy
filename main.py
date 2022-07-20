from flask import Flask, request, render_template, redirect
import os
import model
from model import fscore
app = Flask(__name__)
path_uplaod = r"C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\uploads"
@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        if request.files:
            pdf = request.files['filename']
            pdf.save(os.path.join(path_uplaod, "resume.pdf"))
            print(pdf)
            return render_template('jd.html')
    # else
    # jd = request.form['jd']
    # print(jd)
    # else:
    return render_template('home.html')

@app.route('/jd', methods = ["POST", "GET"])
def jd():
    if request.method == "POST":
        jd = request.form.get('jd')
        print(jd)
        text_file = open(r"C:\Users\ANSHUL SHRIVASTAVA\Desktop\personal\sim\uploads\jd.txt", "w")
        n = text_file.write((jd))
        text_file.close()
        return redirect('/score')
    # else:
    #     return redirect('/')


@app.route('/score', methods = ["GET", "POST"])
def score():
    sim = fscore()
    print(sim)


    return  f" <h1> Your score is {str(sim) } out of 10 </h1>"

if __name__ == "__main__":
    app.run(debug = True)



