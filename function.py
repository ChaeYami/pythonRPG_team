
# ========================== 실행에 필요한 기타 함수 파일 ==========================
import os
from character import *
from random import choices
from time import sleep

star = "\U0001F31F"
dragon = "\U0001F432"
rainbow = "\U0001F308"
stop = "\U0001F6AB"
fairy = "\U0001F9DA"
fire = "\U0001F525"

def start_story():
    sleep(1)
    print(f"\n .. 어느날 르탄이가 공주님을 납치했다!" + dragon) 
    sleep(1)
    print("\n 공주님은 탑 꼭대기에 갇혀있었고...")
    sleep(1)
    print("\n 각 층의 위로 향하는 문 앞에는 매번 문지기들이 지키고 있었다..." + dragon)
    sleep(1)
    input("\n " +fire+ f" 몬스터를 물리치고 탑 꼭대기에 올라 공주님을 구하기 위한 {global_name}용사님의 여정이 시작된다!" +fire)
    sleep(0.5)
    print("\n\n 게임을 시작하기 전에 먼저 직업을 선택하세요")
    sleep(1)
    print("\033[38;2;255;181;216m\n  ------------------------ 직업설명 ------------------------\n\n\033[38;2;255;108;167m▶ 마법사: \033[38;2;255;181;216m기본 마력이 다른 직업에 비해 많습니다. \n특수 공격시 mp -50 | 공격력이 높음. \n\n\033[38;2;255;108;167m▶ 전사: \033[38;2;255;181;216m체력이 높고 기본 공격력이 높음. \n특수공격시 mp -50 | 기본 공격력보다 높은 공격력\n\n\033[38;2;255;108;167m▶ 뱀파이어: \033[38;2;255;181;216m특수공격시 mp -50 \n특수공격의 공격력은 기본공격과 같으나 상대를 공격함과 동시에 자신의 HP를 회복한다. \n(최대 HP와 소모 HP에 비례)\033[0m")

# ---------- 플레이어 이름 받아오기 ----------
global_name = input('\n용사님의 이름을 입력하세요 : ')

# ---------- 직업 선택하기 ----------
global_job = None  # global_job 변수를 먼저 선언하고 None으로 초기화 (안 하면 오류남)


def get_job():  # 직업 선택할 때도 숫자 외의 값에 에러처리 위해 함수로 만듦
    global global_job
    while True:
        try:
            global_job = int(input("\n | 1.마법사 | 2.전사 | 3.뱀파이어 |\n ...  ▶ "))
            break
        except ValueError:
            print("\n숫자로 입력해주세요.\n")

    return global_job

# ---------- 실행시 출력화면 ----------

def start():
    sleep(1)
    print("\n\n -------------------------------------------")
    print(
        "\033[38;2;81;169;255m       "+star+"~용사님의 대모험~"+star+f"       ♥{global_name}용사님♥ \033[0m")
    print(" -------------------------------------------")
    print("\033[38;2;206;149;255m         1. 튜토리얼")
    print("         2. 전투")
    print("         3. 포인트 상점")
    print("         4. 내 정보 보기")
    print("         5. 몬스터 도감")
    print("         6. 종료\033[0m")
    print(" -------------------------------------------")

# ---------- 몬스터들을 저장 ----------

def create_monsters(round):
    Monsters = {}

    Monsters['종민몬'] = Monster('종민몬', round*300+1500, round*500+500, round)
    Monsters['탁근몬'] = Monster('탁근몬', round*300+1500, round*500+1000, round)
    Monsters['영우몬'] = Monster('영우몬', round*300+2000, round*500+500, round)
    Monsters['진규몬'] = Monster('진규몬', round*300+2000, round*500+1000, round)

    return Monsters

# ---------- 플레이어 ----------
Hero = None 
def player_job():
    global Hero
    # num = (round-1)*100
    if global_job == 1:
        Hero = Wizard(global_name, 10000, 2000, 3000, 400, 0 ,1)

    elif global_job == 2:
        Hero = Warrier(global_name, 12000, 2500, 3000, 300, 0 ,1)

    elif global_job == 3:
        Hero = Vampire(global_name, 10000, 2000, 2000, 300, 0 ,1)
        
    return Hero


# ---------- 플레이어 상태 ----------


def show_start(Player):
    sleep(0.5)
    
    n_bars = 20  # 막대의 총 길이
    exp_ratio = (Player.exp)*0.01
    n_filled = int(exp_ratio * n_bars)  # 채워진 막대의 길이
    n_empty = n_bars - n_filled  # 빈 막대의 길이

    bar = "█" * n_filled + " " * n_empty  # 채워진 막대와 빈 막대를 합친 문자열
    
    print("\n\n--------------------------------------------------------------------")
    print(
        f"\033[38;2;255;177;108m          ♥ ♥ {Player.name}용사님 등장!! ♥ ♥\033[0m")
    print("--------------------------------------------------------------------")
    print(
        f"\033[38;2;102;255;178m HP : {Player.hp}/{Player.max_hp} | MP : {Player.mp}/{Player.max_mp} | 공격력 : {int(Player.power)} | 직업 : {Player.job} ")
    print(f"\033[38;2;255;108;167m\n lv : {Player.lv}\033[0m", end='')
    print("   exp |{}| {:.0%}\033[0m".format(bar, exp_ratio)) 
    input("--------------------------------------------------------------------\n")

# ---------- 몬스터 상태 ----------


def show_monster(Monsters,round):
    sleep(0.5)
    print("\033[38;2;255;177;108m\n     탑을 지키는 몬스터들이 등장했다! \n\033[0m")

    for key, name in Monsters.items():  # 몬스터들의 상태 표시

        print(
            f"\033[38;2;255;108;167m    {round}층의 {name.name} \033[38;2;102;255;178m[ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  \033[0m")

# 튜토리얼 선택 시 출력


def skill_info():
    input("\033[38;2;255;181;216m\n\n\n ------------------------ 게임설명 ------------------------\n\n여기는 6층짜리 탑이며, 6층에는 공주님이 잡혀있습니다. \n\n매 층 계단엔 4마리의 몬스터가 있습니다. 모두 무찌르면 다음 라운드로 넘어갈 수 있습니다. \n\n모두 물리치고 공주님을 구해보세요!")
    input("033[38;2;255;181;216m\n\n\n  ------------------------ 직업설명 ------------------------\n\n\033[38;2;255;108;167m▶ 마법사: \033[38;2;255;181;216m기본 마력이 다른 직업에 비해 많습니다. \n특수 공격시 mp -50 | 공격력이 높음. \n\n\033[38;2;255;108;167m▶ 전사: \033[38;2;255;181;216m체력이 높고 기본 공격력이 높음. \n특수공격시 mp -50 | 기본 공격력보다 높은 공격력\n\n\033[38;2;255;108;167m▶ 뱀파이어: \033[38;2;255;181;216m특수공격시 mp -50 \n특수공격의 공격력은 기본공격과 같으나 상대를 공격함과 동시에 자신의 HP를 회복한다. \n(최대 HP와 소모 HP에 비례)")
    input("\033[38;2;255;181;216m\n\n\n ------------------------ 전투 ------------------------\n\n전투는 \033[38;2;102;255;178m몬스터 네 마리와 플레이어 한 명\033[38;2;255;181;216m이 진행하게 되며, 플레이어의 선공으로 시작됩니다. \n\n매 턴마다 공격할 몬스터를 \033[38;2;102;255;178m이름\033[38;2;255;181;216m으로 선택하세요. \n\n\n플레이어는 \033[38;2;102;255;178m일반 공격, 특수 공격\033[38;2;255;181;216m을 선택해서 사용할 수 있습니다.  ")
    print("\033[38;2;255;181;216m\n\n\n ------------------------ 포인트 상점 ------------------------\n\n 전투시 얻은 포인트로 다양한 아이템을 살 수 있습니다. \n\n\n ----------------------- 내 정보 보기 ------------------------\n\n 현재 내 HP, MP, 공격력, 직업 상태를 볼 수 있습니다.  \n\n\n ------------------------ 몬스터 도감 ------------------------\n\n 현재 라운드의 몬스터 HP,공격력 정보를 볼 수 있습니다.\033[0m")


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
        
        # 숫자가 아닌 값을 입력했을 때 예외처리를 위해 전부 정수 처리함
        command = int(
            input('\n ▶ 공격 방법을 선택하세요 (숫자 입력)\n [1. 일반 공격 | 2. 특수 공격 | 3. 전체공격(MP 300 이상 필요)] : '))
        
        if command == int(1):
            other = input('\n ...  ▶ 공격 대상을 선택하세요 (이름입력) : ')
            Player.attack(Monsters[other])
        elif command == int(2):
            other = input('\n ...  ▶ 공격 대상을 선택하세요 (이름입력) : ')
            use_mp(50)
            
        elif command == int(3):
            if Player.mp < 300:  # 마력이 부족한 경우
                print("\n ※ ※ 마력이 부족합니다! ※ ※")
                player_turn(Player, Monsters)
            else:    
                for key, name in Monsters.items():
                    Player.magic_attack(Monsters[name.name])
                         
        else:  # 1, 2 번을 제외한 숫자를 입력했을 때
            sleep(0.5)
            print("알맞은 공격방법을 선택하세요")
            return player_turn(Player, Monsters)
        return Monsters

    except KeyError as e:  # 몬스터 선택 시 이미 죽은 몬스터를 선택했을 때
        sleep(0.5)
        input("선택한 대상이 이미 사망했거나 존재하지 않습니다. 다시 선택하세요")
        player_turn(Player, Monsters)
    except ValueError as v:  # 스킬 선택 시 숫자가 아닌 값을 입력했을 때
        sleep(0.5)
        input("숫자로 입력하세요")
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
    remove_monster = Monsters
    for key, name in list(remove_monster.items()):
        if name.hp <= 0:
            del remove_monster[key]
    if len(remove_monster) <= 0:
        return remove_monster, True
    else:
        return remove_monster, False

# ---------- 플레이어 생존 확인 ----------

def player_death(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

# ---------- 몬스터 도감 ----------

def monster_guide(round):
    Monsters = create_monsters(round)
    print("\n-----------------------------------------")
    print("\033[38;2;74;215;112m ♥몬스터 도감♥\033[0m")
    print("-----------------------------------------")
    for key,name in Monsters.items():
        print(
                f"\033[38;2;255;108;167m {round}층의 {name.name} \033[38;2;102;255;178m[ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  \033[0m")
    input("\n-----------------------------------------")

# ---------- 배틀 ----------

def battle(Hero, Monsters, round):
    while True:
        show_start(Hero)  # 플레이어 상태
        show_monster(Monsters,round)  # 몬스터 상태

        # 플레이어 공격
        Monsters = player_turn(Hero, Monsters)
        sleep(1)

        # 몬스터 체력 확인
        Monsters, game_over = monster_death(Monsters)
        if game_over:
            print("\n==================== 승리 ====================")
            sleep(0.5)
            print("\n이 층의 모든 몬스터를 물리쳤습니다!\n") 
            round += 1
            if round < 6:
                sleep(0.5)
                print("다음 층으로 넘어가려면 전투를 선택하세요") # 03/30 14:46 수정 (문구 추가)
            break
        

        # 몬스터 공격
        Hero = monster_turn(Hero, Monsters)

        # 플레이어 체력 확인
        game_over = player_death(Hero)
        if game_over:
            sleep(0.5)
            print("\n==================== 패배 ====================")
            break
        sleep(1)
    return round


# ---------- 라운드 ----------


def round_play(Hero, round):
    print("\n\n -------------------------------------------------------")
    
    if round == 1:
        
        print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
        print(" -------------------------------------------------------")
        sleep(1)
    elif round == 2:
        sleep(1)
        print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
        print(" -------------------------------------------------------")
        sleep(1)
        print("\n.. 2층으로 올라왔다.")
        sleep(1)
        print("\n 몬스터들이 더 강해져서 돌아왔다!")
    elif round == 3:
        sleep(1)
        print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
        print(" -------------------------------------------------------")
        sleep(1)
        print("\n.. 3층이다... ")
        sleep(1)
        print("\n 몬스터들이 이상한 모습으로 강해진다...")
    elif round == 4:
        sleep(1)
        print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
        print(" -------------------------------------------------------")
        sleep(1)
        print("\n.. 4층에 다다르자 더욱 더 커지고 강해진 몬스터들이 보인다.")
        sleep(1)
        print(f"\n 그렇지만 {global_name}용사님은 포기하지 않지!")
    else:
        sleep(1)
        print(
        f"\033[38;2;81;169;255m                     --{round}층--                    \033[0m")
        print(" -------------------------------------------------------")
        sleep(1)
        print("\n.. 마지막 5층이다. 이 관문을 넘어서면 공주님이 계신 꼭대기에 도착할 수 있다!!")

    Monsters = create_monsters(round)
    return battle(Hero, Monsters, round)


# ---------- 상점 ----------

def store_items(Hero, item, count): # 아이템
    if Hero.point < 100*count:
        print("\n"+"포인트가 부족합니다!")
    else:
        if item == 1:  # 회복물약
            Hero.hp =min(Hero.hp + 500*count, Hero.max_hp) # 최대 hp를 넘기지 않도록
            Hero.point -= 1000*count # 3/30 21:39 가격 1000p로 수정
        if item == 2:  # 강화물약
            Hero.power += 100*count
            Hero.point -= 1000*count
        if item == 3:  # 마법물약
            Hero.mp =min(Hero.hp + 500*count, Hero.max_mp) # 최대 mp를 넘기지 않도록
            Hero.point -= 1000*count


def store(Hero): # 상점
    print("\n"+"*"*15 + "상점" + "*"*15)
    item = 0
    while item != 4:
        print(
            f"\n내 포인트 : {Hero.point}\n1. 회복물약 (1000p) : HP +500\n2. 강화물약 (1000p) : 공격력 +100\n3. 마법물약 (1000p) : mp +100 \n4. 상점 나가기\n")
        print("*"*30)
        item = int(input("구매 할 상품 번호:"))
        if item != 4:
            count = int(input("상품 수량:"))
            store_items(Hero, item, count)
            




def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')