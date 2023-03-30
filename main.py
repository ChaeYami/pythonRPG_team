# 실행파일

from time import sleep
from character import *
from function import *

global_job = get_job()  # 직업 가져오기


def game():

    round = 1
    
    # ---------- 직업 가져와서 저장 (global_job) ----------
    '''
    윤수님 말씀대로 직업 저장 함수가 while 안에 있으면 포인트가 초기화돼서
    얘만 밖으로 뺐더니 잘 되네요!
    '''
    global Hero
    Hero = player_job(round) # 함수로 플레이어 정보 다 받아옴
        
    while 1:
        
        try:  # 수행 행동 숫자 외 선택 시 에러처리
            start()  # 실행시 출력화면

            # ---------- 수행할 행동 선택 ----------
            command = int(input(" ...  ▶ 숫자 선택 : "))

            if command == 1:  # 튜토리얼
                skill_info()

            elif command == 2:  # 전투
                round = round_play(Hero, round)
                if round == 6:
                    print("    공주님을 무사히 구해냈습니다! 당신은 최고의 용사 칭호를 얻었습니다!")
                    break

            elif command == 3:  # 상점
                store(Hero)

            elif command == 4:  # 내 정보 보기
                show_start(Hero)

            elif command == 5:  # 몬스터 도감
                monster_guide(round)

            elif command == 6:  # 종료
                print("게임을 종료합니다.")
                break

            else:
                print("\n올바른 값을 입력해주세요\n")
        except ValueError as e:
            print("\n숫자로 입력해주세요\n")

game()
