# 실행파일

from time import sleep
from character import *
from function import *

global_job = get_job() # 직업 가져오기

def game():
    
    Monsters = create_monsters()
    
    # ---------- 직업 가져와서 저장 (global_job) ----------
    while True:
        
        if global_job == 1:
            Hero = Wizard(global_name, 10000, 2000, 3000, 400)

        elif global_job == 2:
            Hero = Warrier(global_name, 12000, 2500, 3000, 250)

        elif global_job == 3:
            Hero = Vampire(global_name, 10000, 2000, 2000, 250)        
            
        try: # 수행 행동 숫자 외 선택 시 에러처리
            start()  # 실행시 출력화면

            # ---------- 수행할 행동 선택 ----------
            command = int(input(" ...  ▶ 숫자 선택 : "))

            if command == 1:  # 튜토리얼
                skill_info()

            elif command == 2:  # 전투

                while True:
                    show_start(Hero)  # 플레이어 상태
                    show_monster(Monsters)  # 몬스터 상태

                    # 플레이어 공격
                    Monsters = player_turn(Hero, Monsters)
                    sleep(1)

                    # 몬스터 체력 확인
                    Monsters, game_over = monster_death(Monsters)
                    if game_over:
                        print("\n==================== 승리 ====================")
                        print("모든 몬스터를 물리쳤습니다! 게임 종료!")
                        break

                    # 몬스터 공격
                    Hero = monster_turn(Hero, Monsters)

                    # 플레이어 체력 확인
                    game_over = player_death(Hero)
                    if game_over:
                        print("\n==================== 패배 ====================")
                        break
                    sleep(1)

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


game()
