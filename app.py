#현재 데이터를 입력 받는 것 까지 완료

from flask import Flask, render_template,request,redirect,url_for
import os
from flask_sqlalchemy import SQLAlchemy

#데이터 경로
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)
# 데이터 베이스 생성
class chatCreate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100000), nullable=False)

with app.app_context():
    db.create_all()

# 홈 화면
@app.route("/")
def home():
    return "hello"

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
#----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)