class Normal:
    def __init__(self):
        self.mileage = 100  # 기본 마일리지

    # amount to mileage
    def deposit(self, amount):
        self.mileage += amount

    # mileage getter
    def get_mileage(self):
        return self.mileage


class Vip(Normal):
    def __init__(self):
        super().__init__()

    # override
    def deposit(self, amount):
        self.mileage += amount * 2


# customerA, customerB 인스턴스화 (기본 마일리지 100)
customerA = Normal()
customerB = Vip()

# customerA, customerB 각각 어마운트 100씩 추가 적립
customerA.deposit(100)
customerB.deposit(100)

# customerA, customerB 현재 마일리지 출력
print(f'Normal customer A has mileage {customerA.get_mileage()}')
print(f'VIP B has mileage {customerB.get_mileage()}')
