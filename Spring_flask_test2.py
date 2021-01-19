from flask import Flask, request, render_template

app = Flask(__name__)

class Problem:
    def __init__(self, Pnum, Pname, Solved, Pcond, Pdetail, Pinout):
        self.Pnum = Pnum
        self.Pname = Pname
        self.Solved = Solved
        self.Pcond = Pcond
        self.Pdetail = Pdetail
        self.Pinout = Pinout
    def dict(self):
        return {"Pnum" : self.Pnum, "Pname" : self.Pname, "Solved" : self.Solved, "Pcond" : self.Pcond, "Pdetail" : self.Pdetail, "Pinout" : self.Pinout}
    
p_1001 = Problem("1001", "a+b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b 를 입력받아 합을 출력하시오.", "0 < a,b <100", "첫째 줄에 a+b를 출력한다." ], [["20 4"], "24"])
p_1002 = Problem("1002", "a-b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 차을 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다." ], [["20 4"], "16"])
p_1003 = Problem("1003", "a*b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 a*b를 출력한다." ], [["20 4"], "80"])
p_1004 = Problem("1004", "a/b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b 를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다." ], [["20 4"], "5"])
p_1005 = Problem("1005", "a%/b", "Null", ["0.5초", "128MB"],[",2개의 숫자 a,b를 입력받아 나머지을 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다." ], [["20 4"], "0"])

inform={1001:p_1001, 1002:p_1002, 1003:p_1003, 1004:p_1004, 1005:p_1005}

@app.route('/flask_request', methods=['POST'])
def arequest():
    data = request.get_json()
    return getattr(inform[data["Pnum"]],"dict")()

@app.route('/flask_respone', methods=['POST'])
def arespone():
    SubNum = request.get_json()
    Result = request.get_json()
    setattr(inform[SubNum["SubNum"]], "Solved", Result)
    return getattr(inform[SubNum["SubNum"]], "dict")()

if __name__=='__main__':
    app.run(debug=True)