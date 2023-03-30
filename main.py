# 실행파일

from time import sleep
from character import *
from function import *

global_job = get_job()  # 직업 가져오기


def game():

    round = 1

    # ---------- 직업 가져와서 저장 (global_job) ----------
    while True:

        if global_job == 1:
            Hero = Wizard(global_name, 10000, 2000, 3000, 400)

        elif global_job == 2:
            Hero = Warrier(global_name, 12000, 2500, 3000, 250)

        elif global_job == 3:
            Hero = Vampire(global_name, 10000, 2000, 2000, 250)

        while round < 6:

            try:  # 수행 행동 숫자 외 선택 시 에러처리
                start()  # 실행시 출력화면

                # ---------- 수행할 행동 선택 ----------
                command = int(input(" ...  ▶ 숫자 선택 : "))

                if command == 1:  # 튜토리얼
                    skill_info()

                elif command == 2:  # 전투
                    round = round_play(Hero, round)
                    if round == 5:
                        print("몬스터를 모두 물리치고 왕국을 무사히 지켰습니다!")
                    break

                elif command == 3:  # 내 정보 보기
                    show_start(Hero)

                elif command == 4:  # 몬스터 도감
                    monster_guide()

                elif command == 5:  # 종료
                    print("게임을 종료합니다.")
                    break

                else:
                    print("\n올바른 값을 입력해주세요\n")
            except ValueError as e:
                print("\n숫자로 입력해주세요\n")

            if command == 5:
                break


game()
