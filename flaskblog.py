from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e86d8552b05bc0be047aa7c6aba990541a782c3ea86fa9ea571c5d05d221ddfb'


posts = [
    {
        'author':'Shreyansh Shukla', 
        'title':'Streamlit is lit',
        'content':'Streamlit is a great tool for building web apps',
        'date_posted':'March 21, 2024'
    }, 
    {
        'author':'theprimeagen', 
        'title':'Taipy looks promising',
        'content':'Taipy is a good competitor to Streamlit',
        'date_posted':'March 20, 2024'
    }
]

@app.route('/home')
@app.route("/")
def home():
    return render_template('home.html', posts=posts, title='Flask Blog')


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.userName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userNameOrEmail = form.userNameOrEmail.data
        password = form.password.data

        # Check if the input matches either the email or the username
        if (userNameOrEmail == 'admin@blog.com' or 
            userNameOrEmail == 'admin') and password == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)






if __name__ == '__main__':
    app.run(debug=True)