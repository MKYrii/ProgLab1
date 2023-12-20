
class People:
    """содержит данные и работает с ними"""

    groups = {}
    ages = []

    def __init__(self, ages):
        """"считывает информацию из данных файлов"""
        self.ages = list(map(int, ages.split()))
        self.ages.append(124)
        for i in self.ages:
            self.groups[i] = []

    def add_people(self):
        s = input()
        while s != 'END':
            fio, age = s.split(',')
            age = int(age)
            for i in self.ages:
                if age < i:
                    self.groups[i].append([fio, age])
                    break
            s = input()
        for i in range(len(self.ages) - 1, -1, -1):
            if len(self.groups[self.ages[i]]) > 0:
                if self.ages[i] == 124:
                    print('101+: ', end='')
                elif self.ages[i] == self.ages[0]:
                    print(f'0-{self.ages[i]}: ', end='')
                else:
                    print(f'{self.ages[i - 1] + 1}-{self.ages[i]}: ', end='')
                people = self.groups[self.ages[i]]
                people.sort(key=lambda x: x[0])
                people.sort(key=lambda x: x[1], reverse=True)
                for j in people:
                    print(j[0] + ' ' + f'({j[1]})', end='')
                    if j != people[-1]:
                        print(', ', end='')
                print('')


people = People("18 25 35 45 60 80 100")
people.add_people()


