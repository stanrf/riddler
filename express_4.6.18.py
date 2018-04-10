class Attacks(object):

    def __init__(self):
        self.attacknum = 0
        self.attackdate = []
        self.days = {'01' : range(1,32),
                     '02' : range(1,29),
                     '03' : range(1,32),
                     '04' : range(1,31),
                     '05' : range(1,32),
                     '06' : range(1,31),
                     '07' : range(1,32),
                     '08' : range(1,32),
                     '09' : range(1,31),
                     '10' : range(1,32),
                     '11' : range(1,31),
                     '12' : range(1,32),
                     }
        self.years = range (2001,2100)

    def findSolution(self):
        for year in self.years:
            if year % 4 == 0:
                self.days['02'] = range(1, 30)
                year = str(year)
                year = year[2:4]
                year = int(year)
                for key in self.days:
                    for day in self.days[key]:
                        day = int(day)
                        if day * int(key) == year:
                            self.attacknum += 1
                            if year < 10:
                                self.attackdate.append(str(key) + '/' + str(day) + '/' + '0' + str(year))
                            else:
                                self.attackdate.append(str(key) + '/' + str(day) + '/' + str(year))
            else:
                year = str(year)
                year = year[2:4]
                year = int(year)
                for key in self.days:
                    for day in self.days[key]:
                        day = int(day)
                        if day * int(key) == year:
                            self.attacknum += 1
                            if year < 10:
                                self.attackdate.append(str(key) + '/' + str(day) + '/' + '0' + str(year))
                            else:
                                self.attackdate.append(str(key) + '/' + str(day) + '/' + str(year))
        return [self.attacknum, self.attackdate]

if __name__ == '__main__':
    attack = Attacks()
    print("Total attacks  : %d" % attack.findSolution()[0])
    print("Attack dates   : %s" % attack.findSolution()[1])
