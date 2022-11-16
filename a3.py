class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        print(f'\n{self.name} : {self.health}', end='')

    # 피격
    def damaged(self, amount):
        if (self.health <= 0):
            return

        self.health -= amount
        print(f'{self.name} damaged {amount}   :   ', end='')

        if (self.health <= 0):
            print(f'{self.name} destroyed')
        else:
            print(f'{self.name} health : {self.health}')


class Magician(Unit):
    def __init__(self, name, health, energy):
        super().__init__(name, health)
        self.energy = energy
        print(f'({self.energy})')

    # 공격
    def skill(self, energy, target):
        self.energy -= energy
        print(f'{self.name} used skill({energy})   :   ', end='')

        if (self.energy <= 0):
            print('Not enough energy')
        else:
            print(f'{self.energy} energy left')

        target.damaged(20)  # 타겟 피격


# probe, templar 인스턴스화
print('>>>>> Set Units')

probe = Unit('Probe', 40)
templar = Magician('Templar', 80, 200)

# Game Start
print('\n>>>>> Game Start\n')

templar.skill(75, probe)
print('\n')
templar.skill(75, probe)
print('\n')
templar.damaged(10)
print('\n')
templar.skill(75, probe)
