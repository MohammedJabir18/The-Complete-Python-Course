from atm_machine_main.db import Database
from atm_machine_main.atm_main import AtmMachine

db = Database()
atm = AtmMachine()

if __name__ == "__main__":
    db.connection()
    atm.change_pin()
    atm.deposit()
    atm.check_balance()
    atm.withdraw()
    atm.check_balance()

    print("ATM Successfully worked")
