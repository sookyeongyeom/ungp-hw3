class Student:
    def __init__(self, name, height):
        self.create_id(name)
        self.height = height

    # student_id 생성
    def create_id(self, name):
        assembly = ['2021']
        for i, word in enumerate(name.split(' ')):
            initial = word[0]
            ascii = ord(initial)
            with_pad = format(ascii, '03')
            assembly.append(with_pad)
        self.student_id = int(''.join(assembly)) + \
            self.get_full_ascii_sum(name)

    # fullname의 아스키 합
    def get_full_ascii_sum(self, name):
        replaced = name.replace(' ', '')
        sum = 0
        for letter in replaced:
            sum += ord(letter)
        return sum

    # student_id getter
    def get_id(self):
        return self.student_id

    # less than
    def __lt__(self, other):
        return self.height < other.height

    # greater than
    def __gt__(self, other):
        return self.height > other.height

    # equal to
    def __eq__(self, other):
        return self.height == other.height


def boolToString(bool):
    if bool == True:
        return 'True'
    else:
        return 'False'


# students 인스턴스화
peter_parker = Student('Peter Parker', 168)
tony_stark = Student('Tony Stark', 170)
steve_rogers = Student('Steve Rogers', 170)
peter_quill = Student('Peter Quill', 170)
bucky_barnes = Student('Bucky Barnes', 165)

# height 비교
print('>>>>> Compare students\' height\n')

print(f'Peter Parker < Tony Stark : {boolToString(peter_parker < tony_stark)}')

print(
    f'Steve Rogers = Peter Quill : {boolToString(steve_rogers == peter_quill)}')

print(
    f'Peter Quill > Bucky Barnes : {boolToString(peter_quill > bucky_barnes)}')

print(
    f'Tony Stark < Bucky Barnes : {boolToString(tony_stark < bucky_barnes)}')

# student_id 출력
print('\n>>>>> Get all students\' ID\n')

print(f'Peter Parker : {peter_parker.get_id()}')
print(f'Tony Stark : {tony_stark.get_id()}')
print(f'Steve Rogers : {steve_rogers.get_id()}')
print(f'Peter Quill : {peter_quill.get_id()}')
print(f'Bucky Barnes : {bucky_barnes.get_id()}')
