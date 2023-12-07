<<<<<<< Updated upstream
\a
=======
from flask import  Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    post_title = db.Column(db.Text, nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    post_comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'
    
class PostView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100000), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        userid_receive = session.get("user_id")
        title_receive = request.form.get("post_title")
        content_receive = request.form.get("post_content")

        user = User(
            id=userid_receive,
            title=title_receive,
            content=content_receive
            )

        db.session.add(user)
        db.session.commit()
        return render_template('postView.html')


@app.route('/postView', methods=['POST'])
def postView():
    if request.method == 'POST':
    #form에서 보낸 데이터 받아오기
        id_receive = session.get("user_id")
        time_stamp = session.get("time_stamp")
        title_receive = request.form.get("post_title")
        content_receive = request.form.get("post_content")
        comment_receive = request.form.get("post_comment")

    # 데이터를 DB(postview)에 저장하기
        postview = PostView(
            id=id_receive,
            title=title_receive,
            content=content_receive,
            date=time_stamp,
            comment=comment_receive
        )

        db.session.add(postview)
        db.session.commit()

    return render_template('postView.html', data=postview)


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> Stashed changes
