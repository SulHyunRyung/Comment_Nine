from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = secrets.token_hex(16)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    # primary_key=True 는 고유 ID넘버를 주기 위함이고, 
    # autoincrement=True 는 가입할 때 db에 자동으로 증가하게끔 처리
    # unique=true 는 아이디를 생성할 때 고유 ID넘버가 달라도 가입할 수 있는 것을 막음.


with app.app_context():
    db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_password = request.form['user_password']
        # 데이터베이스에서 사용자 조회
        user = User.query.filter_by(
            user_id=user_id, user_password=user_password).first()
        if user:
            session['user_id'] = user.user_id  # 세션에 사용자 ID 저장
            return render_template('index.html')
            #  로그인 성공 시 넘어가는 페이지 ▲
            # return redirect(url_for('index'))

        else:
            flash('아이디 또는 비밀번호를 다시 확인해주세요.', 'error')
            return render_template('login.html')

            # 로그인 실패 시 넘어가는 페이지 ▼
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # 세션에서 사용자 ID 삭제
    return redirect(url_for('index'))


# 회원가입 버튼 눌렀을 때 회원가입 페이지 호출용
@app.route('/join')
def join():
    return render_template('join.html')


# 도움 : 롤넝★ 무한한 감사 // 새로 회원가입할 때
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        user_id_r = request.form['user_id']
        user_password_r = request.form['user_password']

        #  db에 새로운 아이디 저장
        new_user = User(user_id=user_id_r, user_password=user_password_r)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(user_id=user_id_r).first()
        
        if user:
            flash('이미 존재하는 아이디입니다. 다른 아이디를 사용해주세요.')
            return render_template('login.html')
        
        else :
            return render_template('login.html')
        
    flash('회원가입이 완료되었습니다. 로그인해주세요.')
    return render_template('login.html')



# 항상 맨 마지막으로
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
