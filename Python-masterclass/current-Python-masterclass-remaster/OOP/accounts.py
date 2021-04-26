import datetime
import pytz


class Account:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():
        ufc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(ufc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), self.__balance)]
        print(f"Account created for {self._name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than in your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"

            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()}))")


if __name__ == '__main__':
    tim = Account("Tim", 0)
    # tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()
    tim.withdraw(2000)
    tim.show_transactions()
    print("-------------------------------------------------------------------------------------")
    steph = Account("Steph", 800)
    steph.__balance = 200
    print(steph.__dict__)
    steph.deposit(100)
    print(steph.__dict__)
    steph.withdraw(200)
    print(steph.__dict__)
    steph.show_transactions()
    print(steph.__dict__)





