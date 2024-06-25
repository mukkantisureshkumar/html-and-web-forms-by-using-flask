from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired


fai=Flask(__name__)

@fai.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        FD=request.form
        return FD['un']
    return render_template('htmlforms.html')

class nameform(Form):
    sname=StringField(validators=[DataRequired()])
    scollege=TextAreaField()
    sage=IntegerField()
    submit=SubmitField()

@fai.route('/webforms',methods=['GET','POST'])
def webforms():
    enfo=nameform()
    if request.method=='POST':
        nfo=nameform(request.form)
        if nfo.validate():
            return nfo.data


    return render_template('webforms.html',enfo=enfo)










if __name__=='__main__':
    fai.run(debug=True)
