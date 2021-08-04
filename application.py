import flask
from flask import Flask, request, render_template
import sklearn, pickle
import numpy as np
app = Flask(__name__)
knn = pickle.load(open("KNN_Model.sav", "rb"))
@app.route('/')
def index():
    return render_template('CC.html')
@app.route('/predict', methods=['POST'])
def predict():
    
    #answer=[int(x) for x in request.form.values()]
    q1=int(request.form.get('math'))
    q2=int(request.form.get('comunication'))
    q3=int(request.form.get('hours'))
    q4=int(request.form.get('logic'))
    q5=int(request.form.get('hackaton'))
    q6=int(request.form.get('coding'))
    q7=int(request.form.get('public'))
    q8=int(request.form.get('project'))
    q9=int(request.form.get('self-learning'))
    q10=int(request.form.get('extralesson'))
    q11=int(request.form.get('certificate'))
    q12=int(request.form.get('seminar'))
    q13=int(request.form.get('talent'))
    q14=int(request.form.get('olymp'))
    q15=int(request.form.get('writing'))
    q16=int(request.form.get('memory'))
    q17=int(request.form.get('subjects'))
    q18=int(request.form.get('career'))
    q19=int(request.form.get('experience'))
    q20=int(request.form.get('company'))
    q21=int(request.form.get('elder'))
    q22=int(request.form.get('games'))
    q23=int(request.form.get('books'))
    q24=int(request.form.get('goal'))
    q25=int(request.form.get('single'))
    q26=int(request.form.get('behavior'))
    q27=int(request.form.get('otdel'))
    q28=int(request.form.get('motivation'))
    q29=int(request.form.get('hard'))
    q30=int(request.form.get('team'))
    q31=int(request.form.get('introvert'))
    #answer=[np.array(answer)]
    new_h = [q1,q2,q3,q4,q5,q6,q7,q8,
             q9,q10,q11,q12,q13,q14,q15,q16,
             q17,q18,q19,q20,q21,q22,q23,q24,
             q25,q26,q27,q28,q29,q30,q31]
    pr = knn.predict([new_h])
    text1 = ''
    if pr==1:
        text1 ="Design"
    if pr==2:
        text1 ="Manager"
    if pr==0:
        text1 ="Business"
    if pr==3:
        text1 ="Technical"
    
   
    
    return render_template("CC.html", result_text="Result: {}".format(text1))
    
if __name__ == "__main__":
    app.run()
