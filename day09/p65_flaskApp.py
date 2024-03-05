# file: p65_flaskApp.py
# desc: Flask 웹서버

# 명령어 >> pip3 install Flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Flask!!"


@app.route("/unit")
def unit():
    return render_template("unit.html")


@app.route("/naver")
def naver():
    return render_template("register.html")


def main():
    app.run(debug=True, port=8080)  # mac 에서는 80포트같이 낮은 번호로 하면 권한오류뜸.


if __name__ == "__main__":
    main()
