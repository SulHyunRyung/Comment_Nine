from flask import  Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = secrets.token_hex(16)
db = SQLAlchemy(app)

# --------------------------------------------------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    # primary_key=True 는 고유 ID넘버를 주기 위함이고, 
    # autoincrement=True 는 가입할 때 db에 자동으로 증가하게끔 처리
    # unique=true 는 아이디를 생성할 때 고유 ID넘버가 달라도 가입할 수 있는 것을 막음.
with app.app_context():
    db.create_all()


# class PostView(db.Model):
#     id= db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String, nullable=False)
#     time_stamp = db.Column(db.Date, nullable=False)
#     post_title = db.Column(db.Text, nullable=False)
#     post_content = db.Column(db.Text, nullable=False)

# with app.app_context():
#     db.create_all()

class chatCreate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100000), nullable=False)
    #comment = db.Column(db.String(100000))

with app.app_context():
    db.create_all()

# ---------------------------------------------------------------------------------------

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
            return redirect(url_for('show_index'))
            #  로그인 성공 시 넘어가는 페이지 ▲
            # return redirect(url_for('index'))
            # 로그인 실패 시 넘어가는 페이지 ▼
        else:
            flash('아이디 또는 비밀번호를 다시 확인해주세요.', 'error')
            return render_template('login.html')
    return render_template('login.html')

#------------------------------------------------------------------로그인

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # 세션에서 사용자 ID 삭제
    return redirect(url_for('index'))

#----------------------------------------------------------------로그아웃

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

        user = User.query.filter_by(user_id=user_id_r).first()
        
        if user:
            flash('이미 존재하는 아이디입니다. 다른 아이디를 사용해주세요.')
            return render_template('join.html')
        
        else :
            flash('회원가입이 완료되었습니다. 로그인해주세요.')

            #  db에 새로운 아이디 저장
            new_user = User(user_id=user_id_r, user_password=user_password_r)
            db.session.add(new_user)
            db.session.commit()

            return render_template('login.html')

    
    return render_template('login.html')

#---------------------------------------------------------------회원가입

@app.route('/postView', methods=['POST'])
def postView():
    if request.method == 'POST':
    #form에서 보낸 데이터 받아오기
        id_receive = session.get("id")
        comment_receive = request.form.get("comment")

    # 데이터를 DB(postview)에 저장하기
        postview = chatCreate(
            id=id_receive,
            comment=comment_receive
        )

        db.session.add(postview)
        db.session.commit()

    return render_template('postView.html', data=postview)

# 홈 화면
@app.route("/index", methods=['GET','POST'])
def show_index():
    list = db.session.query(User, chatCreate).join(chatCreate, User.user_id == chatCreate.user_id).all()
    chat_list = chatCreate.query.all()
    return render_template('index.html', data=chat_list)

#-----------------------------------------------------------------

#데이터 추가 테이블 화면
@app.route("/content_create", methods=['GET'])
def show_form():
    return render_template('post-add.html')
    
#홈 화면에서 데이터의 값을 테이블에 넣기
@app.route("/api/content_create", methods=['POST'])
def content_create():
    id_receive = request.form.get("id")
    user_id_receive = request.form.get("user_id")
    title_receive = request.form.get("title")
    content_receive = request.form.get("content")

    chatcreate = chatCreate(id=id_receive, user_id=user_id_receive, title=title_receive, content=content_receive)
    db.session.add(chatcreate)
    db.session.commit()

    return redirect(url_for('show_form'))

# -------------------------------------------------------------------------------------------------데이터 추가 완성 라인

# 수정,삭제 화면
@app.route("/edit/", methods=['GET'])
def edit():
    chat_create_list =chatCreate.query.all()
    return render_template('post-edit.html',data=chat_create_list)

#테이블 수정화면에서 데이터 삭제
@app.route("/api/edit/<int:chat_create_id>/", methods=['POST'])
def edit_and_delete(chat_create_id):
    chat_create_list = chatCreate.query.get(chat_create_id)
    if chat_create_list:
        if 'delete' in request.form:
            # 삭제 버튼이 눌렸을 때
            db.session.delete(chat_create_list)
            db.session.commit()
            return redirect(url_for('edit'))  # 삭제 후 목록 페이지로 이동
        elif 'update' in request.form:
            # 수정 폼으로 리다이렉트
            return redirect(url_for('api_update',chat_create_id=chat_create_id))
    return redirect(url_for('edit'))

@app.route("/api/update/<int:chat_create_id>/", methods=['GET'])
def api_update(chat_create_id):
    chat_create_list = chatCreate.query.get(chat_create_id)
    
    if chat_create_list:
        return render_template('post-edit.html', data_to_edit=chat_create_list)

@app.route("/api/update/<int:chat_create_id>/", methods=['POST'])
def update(chat_create_id):
    chat_create_list = chatCreate.query.get(chat_create_id)

    if chat_create_list:
        chat_create_list.title = request.form.get("title")
        chat_create_list.content = request.form.get("content")
        db.session.commit()

    return redirect(url_for('edit'))


# 항상 맨 마지막으로
if __name__ == '__main__':
    app.run(debug=True)
