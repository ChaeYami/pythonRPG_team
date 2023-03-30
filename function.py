
# ========================== 실행에 필요한 기타 함수 파일 ==========================

from character import *
from random import choices
from time import sleep

# ---------- 플레이어 이름 받아오기 ----------
global_name = input('\n용사님의 이름을 입력하세요 : ')

# ---------- 직업 선택하기 ----------
global_job = None  # global_job 변수를 먼저 선언하고 None으로 초기화 (안 하면 오류남)


def get_job():  # 직업 선택할 때도 숫자 외의 값에 에러처리 위해 함수로 만듦
    global global_job
    while True:
        try:
            global_job = int(input("직업선택 | 1.마법사 | 2.전사 | 3.뱀파이어 |\n ...  ▶ "))
            break
        except ValueError:
            print("\n숫자로 입력해주세요.\n")

    return global_job

# ---------- 실행시 출력화면 ----------


def start():
    print("\n\n -------------------------------------------")
    print(
        f"\033[38;2;81;169;255m       ~용사님의 대모험~       ♥{global_name}용사님♥ \033[0m")
    print(" -------------------------------------------")
    print("\033[38;2;206;149;255m         1. 튜토리얼")
    print("         2. 전투")
    print("         3. 내 정보 보기")
    print("         4. 몬스터 도감")
    print("         5. 종료\033[0m")
    print(" -------------------------------------------")

# ---------- 몬스터들을 저장 ----------


def create_monsters(round):
    Monsters = {}

    Monsters['종민몬'] = Monster('종민몬', round*100+500, round*500+500, round)
    Monsters['탁근몬'] = Monster('탁근몬', round*100, round*500, round)
    Monsters['영우몬'] = Monster('영우몬', round*100+1000, round*500+1000, round)
    Monsters['진규몬'] = Monster('진규몬', round*100+500, round*500+500, round)

    return Monsters

# ---------- 라운드가 진행될 때 마다 강해지는 플레이어 ----------
Hero = None 
def player_job(round):
    global Hero
    num = (round-1)*100
    if global_job == 1:
        Hero = Wizard(global_name, 10000+num, 2000+num, 3000+num, 400)

    elif global_job == 2:
        Hero = Warrier(global_name, 12000+num, 2500+num, 3000+num, 250)

    elif global_job == 3:
        Hero = Vampire(global_name, 10000+num, 2000+num, 2000+num, 250)
        
    return Hero

# ---------- 플레이어 상태 ----------


def show_start(Player):
    print("\n\n--------------------------------------------------------------------")
    print(
        f"\033[38;2;255;177;108m          ♥ ♥ {Player.name}용사님 등장!! ♥ ♥\033[0m")
    print("--------------------------------------------------------------------")
    print(
        f"\033[38;2;102;255;178m HP : {Player.hp}/{Player.max_hp} | MP : {Player.mp}/{Player.max_mp} | 공격력 : {Player.power} | 직업 : {Player.job}\033[0m")
    print("--------------------------------------------------------------------\n")

# ---------- 몬스터 상태 ----------


def show_monster(Monsters):
    print("\033[38;2;255;177;108m\n     탑을 지키는 몬스터들이 등장했다! \n\033[0m")

    for key, name in Monsters.items():  # 몬스터들의 상태 표시

        print(
            f"\033[38;2;255;108;167m    {name.name} \033[38;2;102;255;178m[ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  \033[0m")

# 튜토리얼 선택 시 출력


def skill_info():
    print("\033[38;2;255;181;216m\n\n마법사: (설명)\n전사: (설명)\n뱀파이어: (설명)\n\n전투는 \033[38;2;102;255;178m몬스터 네 마리와 플레이어 한 명\033[38;2;255;181;216m이 진행하게 되며, 플레이어의 선공으로 시작됩니다. \n매 턴마다 공격할 몬스터를 \033[38;2;102;255;178m이름\033[38;2;255;181;216m으로 선택하세요. \n\n플레이어는 \033[38;2;102;255;178m일반 공격, 마법 공격, 궁극기\033[38;2;255;181;216m를 선택해서 사용할 수 있습니다. \033[38;2;255;108;167m\n\n일반 공격 : 가장 낮은 공격력 / mp 소모 0\n마법 공격 : 조금 더 강한 공격 / MP 50 소모\n궁극기 : 마법 공격과 함께 체력 회복 / mp 100 소모\n궁극기의 회복량은 소모된 HP에 비례합니다.  \n\n\033[0m")


# ---------- 플레이어 턴 ----------
def player_turn(Player, Monsters):
    # 공격 대상 선택하는 함수

    def use_mp(need):
        if Player.mp < need:  # 마력이 부족한 경우
            print("\n ※ ※ 마력이 부족합니다! ※ ※")
            player_turn(Player, Monsters)
        else:  # 사용가능 - 스킬 사용
            Player.magic_attack(Monsters[other])

    # 몬스터 딕셔너리에 없는 대상을 선택했을 시 예외 처리
    try:
        other = input('\n ...  ▶ 공격 대상을 선택하세요 (이름입력) : ')

        # 숫자가 아닌 값을 입력했을 때 예외처리를 위해 전부 정수 처리함
        command = int(
            input('\n ▶ 공격 방법을 선택하세요 (숫자 입력)\n [1. 일반 공격 | 2. 특수 공격] : '))

        if command == int(1):
            Player.attack(Monsters[other])
        elif command == int(2):
            use_mp(50)
        else:  # 1, 2 번을 제외한 숫자를 입력했을 때
            print("알맞은 공격방법을 선택하세요")
            return player_turn(Player, Monsters)
        return Monsters

    except KeyError as e:  # 몬스터 선택 시 이미 죽은 몬스터를 선택했을 때
        print("선택한 대상이 이미 사망했거나 존재하지 않습니다. 다시 선택하세요")
        player_turn(Player, Monsters)
    except ValueError as v:  # 스킬 선택 시 숫자가 아닌 값을 입력했을 때
        print("숫자로 입력하세요")
        player_turn(Player, Monsters)

# ---------- 몬스터 턴 ----------


def monster_turn(Player, Monsters):
    sleep(1)
    for key, value in Monsters.items():
        commands = ['attack', 'wait']
        weights = [0.7, 0.3]  # 회피 확률
        command = choices(commands, weights=weights)[0]
        if command == 'attack':
            value.attack(Player)
        elif command == 'wait':
            value.wait()

    return Player


# ---------- 몬스터 사망 처리 ----------
def monster_death(Monsters):
    dead_monsters = []
    for key, name in Monsters.items():
        if name.hp <= 0:
            dead_monsters.append(key)

    for name in dead_monsters:
        del Monsters[name]

    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False


# ---------- 플레이어 생존 확인 ----------
def player_death(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

# ---------- 몬스터 ----------


def monster_guide():
    print("\n-----------------------------------------")
    print("\033[38;2;74;215;112m              ♥몬스터 도감♥\033[0m")
    print("-----------------------------------------")
    print("\n종민몬 [ HP : 2000/2000 | 공격력 : 2000]\n탁근몬 [ HP : 3000/3000 | 공격력 : 1000]\n영우몬 [ HP : 4000/4000 | 공격력 : 2000]\n진규몬 [ HP : 5000/5000 | 공격력 : 1500]")
    print("\n-----------------------------------------")

# ---------- 배틀 ----------


def battle(Hero, Monsters, round):
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
            print("\n이 층의 모든 몬스터를 물리쳤습니다!\n") 
            round += 1
            if round < 6:
                print("다음 층으로 넘어가려면 전투를 선택하세요") # 03/30 14:46 수정 (문구 추가)
            break
        

        # 몬스터 공격
        Hero = monster_turn(Hero, Monsters)

        # 플레이어 체력 확인
        game_over = player_death(Hero)
        if game_over:
            print("\n==================== 패배 ====================")
            break
        sleep(1)
    return round


# ---------- 라운드 ----------


def round_play(Hero, round):
    print("\n\n -------------------------------------------------------")
    print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
    if round == 1:
        print(
            f"\n .. 어느날 르탄이가 공주님을 납치했다! \n 몬스터를 물리치고 탑 꼭대기에 올라 공주님을 구하기 위한 {global_name}용사님의 여정이 시작된다!")
    elif round == 2:
        print("\n.. 2층으로 올라왔다. 몬스터들이 더 강해져서 돌아왔다!")
    elif round == 3:
        print("\n.. 3층이다... 몬스터들이 이상한 모습으로 강해진다...")
    elif round == 4:
        print(f"\n.. 4층에 다다르자 더욱 더 커지고 강해진 몬스터들이 보인다. 그렇지만 {global_name}용사님은 포기하지 않지!")
    else:
        print("\n.. 마지막 5층이다. 이 관문을 넘어서면 공주님이 계신 꼭대기에 도착할 수 있다!!")

    Monsters = create_monsters(round)
    return battle(Hero, Monsters, round)
