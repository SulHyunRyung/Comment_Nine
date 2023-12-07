from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import secrets


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = secrets.token_hex(16)   

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('index.html')
    else:
        return render_template('index.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login_post():
    user_id = request.form['user_id']
    user_password = request.form['user_password']

    # 데이터베이스에서 사용자 조회
    user = User.query.filter_by(user_id=user_id, user_password=user_password).first()

    if user:
        session['user_id'] = user.user_id  # 세션에 사용자 ID 저장
        return redirect(url_for('index'))
    else:
        flash('아이디 또는 비밀번호를 다시 확인해주세요.', 'error')
        return render_template('login.html')

@app.route('/logout' , methods=['POST'])
def logout():
    session.pop('user_id', None)  # 세션에서 사용자 ID 삭제
    return redirect(url_for('index'))

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)