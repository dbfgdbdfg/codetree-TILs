class Code:
    def __init__(self,secret_code,meeting_point,time):
        self.secret_code=secret_code
        self.meeting_point=meeting_point
        self.time=time
w=input().split()
first=Code(w[0],w[1],w[2])
print("secret code : "+first.secret_code)
print("meeting point : "+first.meeting_point)
print("time : "+first.time)