from character import *
from random import choices
from time import sleep

# ========================== 게임 진행 함수 ==========================


def create_monsters():  # 몬스터들을 저장
    
    
    Monsters = {}
    
    Monsters['종민몬'] = Monster('종민몬', 2000, 2000)
    Monsters['탁근몬'] = Monster('탁근몬', 3000, 1000)
    Monsters['영우몬'] = Monster('영우몬', 4000, 2000)
    Monsters['진규몬'] = Monster('진규몬', 5000, 1500)

    return Monsters


# 플레이어와 몬스터들의 상태
def show_start(Player):
    print("\n\n---------------------------------------------------------------")
    print(f"\033[38;2;255;177;108m          ♥ ♥ {Player.name}용사님 등장!! ♥ ♥\033[0m")
    print("--------------------------------------------------------------------")
    print(
        f"\033[38;2;102;255;178m   HP : {Player.hp}/{Player.max_hp} | MP : {Player.mp}/{Player.max_mp} | 공격력 : {Player.power} | 직업 : {Player.job}\033[0m")
    print("--------------------------------------------------------------------\n")
    
    
def show_monster(Monsters):
    print("\033[38;2;255;177;108m\n     야생의 몬스터들이 등장했다! \n\033[0m")

    for key, name in Monsters.items():  # 몬스터들의 상태 표시

        print(f"\033[38;2;255;108;167m    {name.name} \033[38;2;102;255;178m[ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  \033[0m")
        
        
        
        
def skill_info():
    print("\033[38;2;255;181;216m\n\n마법사: (설명)\n전사: (설명)\n뱀파이어: (설명)\n\n전투는 \033[38;2;102;255;178m몬스터 네 마리와 플레이어 한 명\033[38;2;255;181;216m이 진행하게 되며, 플레이어의 선공으로 시작됩니다. \n매 턴마다 공격할 몬스터를 \033[38;2;102;255;178m이름\033[38;2;255;181;216m으로 선택하세요. \n\n플레이어는 \033[38;2;102;255;178m일반 공격, 마법 공격, 궁극기\033[38;2;255;181;216m를 선택해서 사용할 수 있습니다. \033[38;2;255;108;167m\n\n일반 공격 : 가장 낮은 공격력 / mp 소모 0\n마법 공격 : 조금 더 강한 공격 / MP 50 소모\n궁극기 : 마법 공격과 함께 체력 회복 / mp 100 소모\n궁극기의 회복량은 소모된 HP에 비례합니다.  \n\n\033[0m")

# ---------- 플레이어 턴 ----------


def player_turn(Player, Monsters):
    # 공격 대상 선택하는 함수

    def use_mp(need):
        if Player.mp < need:  # 마력이 부족한 경우
            print("\n ※ ※ 마력이 부족합니다! ※ ※")
            player_turn(Player, Monsters)
        else: # 사용가능 - 스킬 사용
            Player.magic_attack(Monsters[other])
            
    # 몬스터 딕셔너리에 없는 대상을 선택했을 시 예외 처리
    try:
        other = input('\n ...  ▶ 공격 대상을 선택하세요 (이름입력) : ')

        command = int(input('\n ▶ 공격 방법을 선택하세요 (숫자 입력)\n [1. 일반 공격 | 2. 특수 공격] : '))

        if command == int(1):
            Player.attack(Monsters[other])
        elif command == int(2):
            use_mp(50)
        else:
            print("알맞은 공격방법을 선택하세요")
            return player_turn(Player, Monsters)
        return Monsters
    
    except KeyError as e:  # 이미 죽은 몬스터를 선택했을 때
        print("선택한 대상이 이미 사망했거나 존재하지 않습니다. 다시 선택하세요")
        player_turn(Player, Monsters)
    except ValueError as v:
        print("숫자로 입력하세요")
        player_turn(Player, Monsters)

    
    

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

# ---------- 플레이어 생존 확인 ----------
def player_death(Player):
    if Player.hp <= 0:
        return True
    else:
        return False

