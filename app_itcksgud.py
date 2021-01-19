from flask import Flask, render_template, request

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
p_1003 = Problem("1003", "ab", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 ab를 출력한다." ], [["20 4"], "80"])
p_1004 = Problem("1004", "a/b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b 를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다." ], [["20 4"], "5"])
p_1005 = Problem("1005", "a%/b", "Null", ["0.5초", "128MB"],[",2개의 숫자 a,b를 입력받아 나머지을 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다." ], [["20 4"], "0"])
plist=[p_1001,p_1002,p_1003,p_1004,p_1005]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/pro1', methods=['POST'])
def pro1():
    data = request.get_json()["Pnum"]
    return getattr(plist[data-1001],"dict")()

@app.route('/pro2', methods=['POST'])
def pro2():
    data = request.get_json()["Pnum"]
    Sol = request.get_json()["Result"]
    setattr(plist[data-1001],"Solved",Sol)
    return getattr(plist[data-1001],"dict")()

if __name__ == '__main__':
    app.run(debug=True)

"""
1.스프링으로 부터 문제 번호가 넘어오면 그에 해당하는 정보를 getattr을 통해 반환해줌
( spring과 flask README.md확인 , 카톡에 올려준 사이트를 이용해 json 형식으로 flask로 보내고 json형식으로 다시 필요한 정보반환 되는지 확인)
2.Spring으로부터 제출결과가 넘어오면 Solved setattr을 통해 수정
"""