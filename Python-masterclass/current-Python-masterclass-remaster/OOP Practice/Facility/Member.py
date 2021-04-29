class Member(object):

    def __init__(self, name=None, id_num=None, membership_type=None, balance=0, weight=None, height=None, trainer=None):
        self.name = name
        self.id_num = id_num
        self.membership_type = membership_type
        self.balance = balance
        self.weight = weight
        self.height = height
        self.trainer = trainer
        self.facilityList = []

    def getWeight(self):
        return self.weight

    def set_weight(self, newWeight):
        self.weight += newWeight

    def getHeight(self):
        return self.height

    def getTrainer(self):
        return self.trainer

    def registerTrainer(self, trainer):
        self.trainer = trainer

    def referTrainer(self, otherM):
        self.trainer = otherM.getTrainer()

    def registerFacility(self, facility):
        self.facilityList.append(facility)

    def getPaymentDue(self):
        total = 0
        for facility in self.facilityList:
            total += (facility.get_unit() * facility.get_price())
        return total

    def swapTrainer(self, otherM):
        self.trainer, otherM.trainer = otherM.trainer, self.trainer

    def getBMIReport(self):
        self.bmi = self.weight / ((self.height / 100) ** 2)
        result = ''
        if self.bmi < 18.5:
            result = f'Underweight ({self.bmi:.1f})'
        elif 18.5 < self.bmi < 24.9:
            result = f'Normal ({self.bmi:.1f})'
        elif 25 < self.bmi < 29.9:
            result = f'Overweight ({self.bmi:.1f})'
        else:
            result = f'Obese ({self.bmi:.1f})'

        return result

    @classmethod
    def constructor2(cls, id_num, ty, balance):
        return cls(name=None, id_num=id_num, membership_type=ty, balance=balance)

    @classmethod
    def constructor3(cls, weight, height):
        return cls(name=None, id_num=None, membership_type=None, balance=0, weight=weight, height=height)

    @classmethod
    def constructor4(cls, name):
        return cls(name=name, id_num=None, membership_type=None, balance=0, weight=None, height=None)


class Trainer:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Facility:

    def __init__(self, facilityName, unit, price):
        self.facilityName = facilityName
        self.unit = unit
        self.price = price

    def get_unit(self):
        return self.unit

    def get_price(self):
        return self.price

















