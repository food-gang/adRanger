from flask import Flask,render_template,session,redirect,url_for,send_file,send_from_directory
from randomprog import getArray
from flask import request
import os
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app=Flask(__name__)
app.config['SECRET_KEY']='Salam aleikym'



class SearchForm(Form):
    query=StringField('Search')

@app.route('/', methods=['GET', 'POST'])
def search():
    form=SearchForm(request.form)
    if request.method=='POST':
        #try:
            query=str(form.query)
            one=query.find("value=")
            end=query.find(">")
            print(query[one+7:end-1])
            getArray(query[one+7:end-1])
            #response = send_from_directory(directory='static/js', filename='data_file.json')
            return render_template("Index.html", form=form)
        #except:
            print('Your request is bad:/')
    return render_template("Index.html", form=form)
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response
if __name__=='__main__':
    app.run()
extra_dirs = ['static/',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)
app.run(extra_files=extra_files)
