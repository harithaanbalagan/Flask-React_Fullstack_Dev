
from flask import Flask, render_template, request, redirect, url_for
from forms import Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route("/", methods=['GET','POST'])
def hello_world():
    request_method=request.method
    if request.method=='POST':
        print("--------------")
        print(request.form)
        print("---------------")
        firstname=request.form['f_name']
        return redirect(url_for('name',firstname=firstname))
    return render_template('hello.html',request_method=request_method,list_of_names=['hi'])

@app.route("/name/<string:firstname>")
def name(firstname):
    return f'redirected page {firstname}'

@app.route('/todo',methods=['GET','POST'])
def todo():
    todp_form= Todo()
    print("logged")
    if todp_form.validate_on_submit():
        print(todp_form.content.data)
        return redirect("/")
    return render_template('Todo.html',form=todp_form)


if __name__ == "__main__":
    app.run(debug=True)