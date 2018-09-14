from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    # return render_template('test.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            # 渲染后category参数会变成message的classname,相应的修改class的css即可修改显示效果
            flash('You were successfully logged in', category='info')
            flash('test error', category='error')
            print('IN')
            # return redirect(url_for('index'))
    return render_template('test.html', error=error)


app.run(debug=True)
