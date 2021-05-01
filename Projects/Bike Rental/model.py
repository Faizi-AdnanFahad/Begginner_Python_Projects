import datetime

class BikeRental:

    def __init__(self, bikeStock=0):
        self.bikeStock = bikeStock
        self.currentHour = datetime.time.hour

    def displaystock(self):
        return self.bikeStock

    def rentBikeOnHourlyBasis(self, numOfHours):
        # date.hour from the moment bought
        result = None
        if 0 < numOfHours <= self.bikeStock:
            result = datetime.datetime.now()

        return result

    def rentBikeOnDailyBasis(self, numOfDays):
        result = None
        if 0 < numOfDays <= self.bikeStock:
            result = datetime.datetime.now()

        return result

    def rentBikeOnWeeklyBasis(self, numOfWeeks):
        result = None
        if 0 < numOfWeeks <= self.bikeStock:
            result = datetime.datetime.now()

        return result

    def returnBike(self, customerObj):
        return None

    @classmethod
    def constructor2(cls, bikeStock):
        return cls(bikeStock=bikeStock)


class Customer:

    def __init__(self):
        pass

    def returnBike(self):
        pass





















