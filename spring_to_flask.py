from flask import Flask, render_template, request
import Class_flask
from Class_flask import Problem
from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)

p_1001 = Problem(1001, "a+b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 합을 출력하시오.", "0 < a,b <100", "첫째 줄에 a+b를 출력한다."], [["20 4"], "24"])
p_1002 = Problem(1002, "a-b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 차를 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다."], [["20 4"], "16"])
p_1003 = Problem(1003, "a*b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 a*b를 출력한다."], [["20 4"], "80"])
p_1004 = Problem(1004, "a/b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다."], [["20 4"], "5"])
p_1005 = Problem(1005, "a%/b", "Null", ["0.5초", "128MB"],
                 ["2개의 숫자 a,b를 입력받아 나머지를 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다."], [["20 4"], "0"])

Problems = {1001: p_1001, 1002: p_1002, 1003: p_1003, 1004: p_1004, 1005: p_1005}  # 문제번호를 통해 클래스를 쉽게 찾을 수 있도록 딕셔너리 생성


@app.route("/", methods=["get"])
def hi():
    k = Problems.keys()
    l = []
    for i in k:
        q = Problems[i].Pname
        re = Problems[i].Solved

        l.append((i, q, re))
    print(l)
    return jsonify(l)


@app.route("/flask_Problem_info", methods=["POST"])
def flask_Problem_info():
    # print(request)
    problem = request.get_json()
    # print(problem)
    print(getattr(Problems[problem["Pnum"][0]], "dict")())
    return getattr(Problems[problem["Pnum"][0]], "dict")()




user_sub_info = []
@app.route("/flask_Submit", methods=["POST"])
def flask_Submit():
    submit = request.get_json()
    # print(submit)
    user_sub_info.append([submit["SubNum"][0], submit["Pnum"][0]])
    # print(user_sub_info)
    return "hi"


@app.route("/flask_submit_result", methods=["POST"])
def flask_submit_result():
    result = request.get_json()
    # print(result)
    # setattr(Problems[result["SubNum"][0]], "Solved", result["Result"][0])      # SubNum이 없어 Pnum이랑 동일 취급 후 코드 작성
    return "HAWI"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)