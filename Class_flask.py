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
