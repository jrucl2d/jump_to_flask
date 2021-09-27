from flask import Flask, url_for, request, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'really_secret_key'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''
참고 : https://flask.palletsprojects.com/en/2.0.x/quickstart/
path variable : string, int, float, path, uuid
매칭되지 않을 경우 404 error
'''
# default로 string
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# string : string인 username
@app.route("/user/<string:username>")
def show_user_profile(username):
    return f"User {escape(username)}"

# int : integer인 post_id
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

# float : 양수인 부동 소수점을 갖는 실수
@app.route("/money/<float:money>")
def show_money(money):
    return f"$ {money}"

# path : string과 같지만 /를 포함 가능
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return f"POST login request"
    else:
        # 쿼리 스트링의 key에 해당하는 값이 없으면 nokey로 출력됨
        searchWord = request.args.get('key', 'nokey')
        session['username'] = 'login'
        return f"POST login request / key : {searchWord}"

@app.route("/cookie/get")
def cookie_get():
    # cookies[key]로 사용할 시 값이 없으면 KeyError 발생
    cookie = "noCookie" if request.cookies.get('username') == None else "yesCookie"
    return cookie

@app.route('/session/check')
def session_check():
    if 'username' in session:
        return f'로그인 된 유저 : {session["username"]}'
    return 'Not logged in'

# url_for을 사용해서 url 생성
with app.test_request_context():
    print(url_for('show_user_profile', username='HaHaMan'))
    print(url_for('show_money', money=11.4))
    print(url_for('hello_world', custom="ha1", custom2="ha2")) # 쿼리 스트링 ?custom=ha1&custom2=ha2

# python3 app.py로 실행할 때
if __name__ == "__main__":
    app.run(debug=True, use_debugger=True, use_reloader=True)