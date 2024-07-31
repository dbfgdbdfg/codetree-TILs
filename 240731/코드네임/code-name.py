class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

def main():
    agents = []

    # 5명의 요원 정보를 입력받음
    #print("Enter 5 agents' codename and score, each on a new line:")
    for _ in range(5):
        # 입력받기
        input_line = input().strip()
        codename, score = input_line.split()
        score = int(score)
        agents.append(Agent(codename, score))
    
    # 점수가 가장 낮은 요원을 찾기
    lowest_score_agent = min(agents, key=lambda agent: agent.score)
    
    # 결과 출력
    print(f"{lowest_score_agent.codename} {lowest_score_agent.score}")

if __name__ == "__main__":
    main()

"""
Agent 클래스:

__init__ 메소드: codename과 score를 초기화합니다.
__str__ 메소드는 제거하여 출력 형식에 영향을 주지 않도록 합니다.
main 함수:

사용자로부터 5명의 요원 정보를 줄 단위로 입력받습니다.
입력값을 codename과 score로 분리하고, score를 정수로 변환한 후, Agent 객체로 리스트에 추가합니다.
min 함수를 사용하여 점수가 가장 낮은 요원을 찾습니다.
찾은 요원의 코드네임과 점수를 print를 통해 공백으로 구분하여 출력합니다.
"""