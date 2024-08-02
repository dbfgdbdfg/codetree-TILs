n=int(input())

class Hight:
    def __init__(self,key,hight,sun):
        self.key, self.hight, self.sun=key, hight, sun

for i in range(n):
    key,hight=tuple(input().split())
    sun=i+1


for i in range(n):
    


'''
#ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())

    # Forecast 객체를 만들어 줍니다.
    f = Forecast(date, day, weather)
    if weather == "Rain":
        # 비가 오는 경우 가장 최근인지 확인하고,
        # 가장 최근일 경우 정답을 업데이트합니다.
        if ans.date >= f.date:
            ans = f

# 결과를 출력합니다.
print(ans.date, ans.day, ans.weather)
'''