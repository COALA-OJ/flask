from flask import Flask, render_template, request
import Class_flask
from Class_flask import Problem
from flask import Flask, jsonify
import db


app = Flask(__name__)

p_1001 = Problem(1001, "a+b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 합을 출력하시오.", "0 < a,b <100", "첫째 줄에 a+b를 출력한다."], [["20 4"], "24"])
p_1002 = Problem(1002, "a-b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 차를 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다."], [["20 4"], "16"])
p_1003 = Problem(1003, "a*b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 a*b를 출력한다."], [["20 4"], "80"])
p_1004 = Problem(1004, "a/b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다."], [["20 4"], "5"])
p_1005 = Problem(1005, "a%%b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 나머지를 출력하시오.", "0 < a,b <100", "첫째 줄에 a%%b를 출력한다."], [["20 4"], "0"])

Problems = {1001: p_1001, 1002: p_1002, 1003: p_1003, 1004: p_1004, 1005: p_1005}  # 문제번호를 통해 클래스를 쉽게 찾을 수 있도록 딕셔너리 생성

# 회원가입 - 아이디 중복 여부
@app.route("/id_check", methods=["POST"])
def id_check():
    data = request.get_json()
    id = data["ID"]
    
    db_class = db.Database()
    sql = f"SELECT id FROM test_db.user WHERE id='{id}'"
    row = db_class.executeAll(sql)

    if len(row)>0 and row[0]['id']==id:
        return jsonify(ID="False")
    else:
        return jsonify(ID="True")


# 회원가입 - 회원 가입 요청
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    id = data["ID"]
    pw = data["Pwd"]
    name = data["Name"]
    
    db_class = db.Database()
    sql = f"INSERT INTO test_db.user VALUES ('{id}', '{pw}', '{name}')"
    try:
        db_class.execute(sql)
        db_class.commit()
    except:
        return jsonify(result="False")
    return jsonify(result="True")


# 로그인
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    id = data["ID"]
    pw = data["Pwd"]
    
    db_class = db.Database()
    sql = f"SELECT id FROM test_db.user WHERE id='{id}' AND pw='{pw}'"
    row = db_class.executeAll(sql)

    if len(row)>0:
        return jsonify(result="True")
    else:
        return jsonify(result="False")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)