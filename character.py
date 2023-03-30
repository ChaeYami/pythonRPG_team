# 플레이어, 몬스터 정의 클래스 파일

import random

# ========================== 플레이어 (직업) ==========================


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    # 공격 함수 - 플레이어의 일반공격과 몬스터의 공격에서 모두 사용
    def __init__(self, name, hp, power, magic_power, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        self.level = 1  # 레벨 초기값
        self.exp = 0  # 경험치 초기값
        self.max_exp = 50  # 레벨업을 위한 최대 경험치

    # 공격 함수 - 플레이어의 일반공격과 몬스터의 공격에서 모두 사용
    def attack(self, other):
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            self.exp += 50  # 쓰러진 적으로부터 경험치 얻음
            while self.exp >= self.max_exp:  # 경험치가 최대치 이상일 경우 레벨업
                self.level += 1
                self.max_hp += 50
                self.hp = self.max_hp
                self.power += 10
                self.magic_power += 10
                self.max_mp += 50
                self.mp = self.max_mp
                self.exp -= self.max_exp
                self.max_exp += 50
                print(f"\n레벨업! {self.name}이(가) 레벨 {self.level}이 되었습니다!")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    # 상태창
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}, 레벨 {self.level}, 경험치 {self.exp}/{self.max_exp}")
    # 상태창

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Wizard(Character):
    def __init__(self, name, hp, power, magic_power, mp):
        super().__init__(name, hp, power, magic_power, mp)

        self.job = '마법사'  # 콘솔 출력을 위한 문자열

    def magic_attack(self, other):  # 특수공격
        # 특수공격 데미지
        magic_damage = random.randint(
            self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)
        print(
            f"\033[38;2;161;196;255m\n .. 매직 익스플로전!!! | MP -100 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")

        self.mp -= 100  # mp 소모

        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            self.exp += 50  # 쓰러진 적으로부터 경험치 얻음
            while self.exp >= self.max_exp:  # 경험치가 최대치 이상일 경우 레벨업
                self.level += 1
                self.max_hp += 50
                self.hp = self.max_hp
                self.power += 10
                self.magic_power += 10
                self.max_mp += 50
                self.mp = self.max_mp
                self.exp -= self.max_exp
                self.max_exp += 50
                print(f"\n레벨업! {self.name}이(가) 레벨 {self.level}이 되었습니다!")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    def show_status(self):  # 상태 출력
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


"""
전사 클래스 : 체력 12000, 공격력 2500, 특수공격력 3000, 마력 250, 특수공격시 마력소모량 50
스킬 : 몸통박치기! >> 강한 공격
"""


class Warrier(Character):
    def __init__(self, name, hp, power, magic_power, mp):
        super().__init__(name, hp, power, magic_power, mp)

        self.job = '전사'  # 콘솔 출력을 위한 문자열

    def magic_attack(self, other):
        magic_damage = random.randint(
            self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)

        print(
            f"\033[38;2;161;196;255m\n .. 몸통박치기! | MP -50 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")

        self.mp -= 50

        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            self.exp += 50  # 쓰러진 적으로부터 경험치 얻음
            while self.exp >= self.max_exp:  # 경험치가 최대치 이상일 경우 레벨업
                self.level += 1
                self.max_hp += 50
                self.hp = self.max_hp
                self.power += 10
                self.magic_power += 10
                self.max_mp += 50
                self.mp = self.max_mp
                self.exp -= self.max_exp
                self.max_exp += 50
                print(f"\n레벨업! {self.name}이(가) 레벨 {self.level}이 되었습니다!")
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

        self.job = '뱀파이어'  # 콘솔 출력을 위한 문자열

    def magic_attack(self, other):
        # 특수공격 데미지
        magic_damage = random.randint(
            self.magic_power * 0.9, self.magic_power * 1.5)

        # 회복량 - 소모 체력에 비례
        heal_amount = int((self.max_hp-self.hp) * 0.4)

        other.hp = max(other.hp - magic_damage, 0)

        print(
            f"\033[38;2;161;196;255m\n .. 흡혈! | MP -50 | {other.name}에게 {magic_damage}의 피해를 주었습니다! \n .. 체력을 {heal_amount}만큼 회복했습니다.({self.hp}/{self.max_hp})\033[0m")

        self.hp += heal_amount  # 회복
        self.mp -= 50  # mp 소모

        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            self.exp += 50  # 쓰러진 적으로부터 경험치 얻음
            while self.exp >= self.max_exp:  # 경험치가 최대치 이상일 경우 레벨업
                self.level += 1
                self.max_hp += 50
                self.hp = self.max_hp
                self.power += 50
                self.magic_power += 50
                self.max_mp += 50
                self.mp = self.max_mp
                self.exp -= self.max_exp
                self.max_exp += 50
                print(f"\n레벨업! {self.name}이(가) 레벨 {self.level}이 되었습니다!")

        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


# ========================== 몬스터 ==========================
class Monster(Character):
    def __init__(self, name, hp, power, round):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.round = round

    def wait(self):  # 회피함수
        print(f'\n\033[38;2;255;156;166m .. {self.name}의 공격이 빗나갔다!!\033[0m')
