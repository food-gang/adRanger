from flask import Flask,render_template
from randomprog import getArray
from flask import request

from wtforms import Form, BooleanField, StringField, PasswordField, validators

app=Flask(__name__)
app.config['SECRET_KEY']='Salam aleikym'



class SearchForm(Form):
    query=StringField('Search')

@app.route('/', methods=['GET', 'POST'])
def serach():
    form=SearchForm(request.form)
    if request.method=='POST':
        try:
            query=str(form.query)
            one=query.find("value=")
            end=query.find(">")
            print(query[one+7:end-1])
            getArray(query[one+7:end-1])
        except:
            print('Your request is bad:/')
    return render_template('Index.html', form=form)
@app.route('/')
def index():
    return render_template('Index.html')
if __name__=='__main__':
    app.run()
