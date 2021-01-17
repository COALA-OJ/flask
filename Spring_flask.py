from flask import Flask, render_template, request

app = Flask(__name__)

class Problem:                                                   # 각 문제마다 가진 정보를 저장할 클래스 생성 
    def __init__(self,Pnum,Pname,Solved,Pcond,Pdetail,Pinout):
        self.Pnum = Pnum
        self.Pname = Pname
        self.Solved = Solved
        self.Pcond = Pcond
        self.Pdetail = Pdetail
        self.Pinout = Pinout

    def dict(self):
        return {"Pnum" : [self.Pnum], "Pname" : self.Pname, "Solved" : self.Solved, "Pcond" : self.Pcond, "Pdetail" : self.Pdetail, "Pinout" : self.Pinout}

p_1001 = Problem(1001, "a+b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 합을 출력하시오.", "0 < a,b <100", "첫째 줄에 a+b를 출력한다." ], [["20 4"], "24"])
p_1002 = Problem(1002, "a-b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 차를 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다." ], [["20 4"], "16"])
p_1003 = Problem(1003, "a*b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 a*b를 출력한다." ], [["20 4"], "80"])
p_1004 = Problem(1004, "a/b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다." ], [["20 4"], "5"])
p_1005 = Problem(1005, "a%b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 나머지를 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다." ], [["20 4"], "0"])

Problems = {1001 : p_1001, 1002 : p_1002, 1003 : p_1003, 1004 : p_1004, 1005 : p_1005}      # 문제번호를 통해 클래스를 쉽게 찾을 수 있도록 딕셔너리 생성

@app.route("/flask_request", methods = ["POST"])
def flask_request():
    problem = request.get_json()
    return getattr(Problems[problem["Pnum"][0]], "dict")()

@app.route("/flask_response", methods = ["POST"])
def flask_response():
    result = request.get_json()
    setattr(Problems[result["SubNum"][0]], "Solved", result["Result"][0])      # SubNum이 없어 Pnum이랑 동일 취급 후 코드 작성
    return getattr(Problems[result["SubNum"][0]], "dict")()

if __name__ == "__main__":
    app.run(debug = True)