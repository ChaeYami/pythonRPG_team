import random



# ---------- 플레이어 이름 받아오기 ----------
global_name = input('\n용사님의 이름을 입력하세요 : ')


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """
    def __init__(self, name, hp, power, magic_power, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power

    def attack(self, other): 
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    def magic_attack(self,other):
        damage = random.randint(self.power * 0.8, self.power * 1.5)
        other.hp = max(other.hp - damage, 0)
        print(f"\033[38;2;161;196;255m\n .. 특수공격 | MP -50 | {other.name}에게 {damage}의 피해를 주었습니다!\033[0m")
        self.mp -= 50
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")   

  
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        
        
        
"""
마법사 클래스 : 체력 10000, 공격력 2000, 특수공격력 3000, 마력 400, 특수공격시 마력소모량 100
스킬 : 매직 익스플로전!!! >> 강한 공격
"""


class Wizard(Character):
    def __init__(self, name, hp, power, magic_power, mp):
        super().__init__(name, hp, power, magic_power, mp)
        
        self.job = '마법사'
    

        
    def magic_attack(self,other):
        magic_damage = random.randint(self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)
        print(f"\033[38;2;161;196;255m\n .. 매직 익스플로전!!! | MP -100 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")
        self.mp -= 100
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")    
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")
            
"""
전사 클래스 : 체력 12000, 공격력 2500, 특수공격력 3000, 마력 250, 특수공격시 마력소모량 50
스킬 : 몸통박치기! >> 강한 공격
"""    

class Warrier(Character):
    def __init__(self, name, hp, power, magic_power, mp):
        super().__init__(name, hp, power, magic_power, mp)
        self.job = '전사'
   
    def magic_attack(self,other):
        magic_damage = random.randint(self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)
        print(f"\033[38;2;161;196;255m\n .. 몸통박치기! | MP -50 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")
        self.mp -= 50
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")    
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")
            
"""
뱀파이어 클래스 : 체력 10000, 공격력 2000, 특수공격력 2000, 마력 250, 특수공격시 마력소모량 50
스킬 : 흡혈! >> 상대의 hp를 깎고 본인의 hp를 회복(hp소모량의 40%)
"""    

class Vampire(Character):
    def __init__(self, name, hp, power, magic_power, mp):
        super().__init__(name, hp, power, magic_power, mp)
        self.job = '뱀파이어'
        
    def magic_attack(self,other):
        magic_damage = random.randint(self.magic_power * 0.9, self.magic_power * 1.5)
        exhausted_hp = self.max_hp-self.hp
        heal_amount = int(exhausted_hp * 0.4)
        self.hp += heal_amount
        self.mp -= 50
        print(f"\033[38;2;161;196;255m\n .. 흡혈! | {other.name}에게 {magic_damage}의 피해를 주었습니다! \n .. 체력을 {heal_amount}만큼 회복했습니다.({self.hp}/{self.max_hp})\033[0m")
        print(f" .. 남은 마력: {self.mp}/{self.max_mp}")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")    
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


# ========================== 몬스터 ==========================
class Monster(Character):
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power




    def wait(self):
        print(f'\n\033[38;2;255;156;166m .. {self.name}의 공격이 빗나갔다!!\033[0m')

