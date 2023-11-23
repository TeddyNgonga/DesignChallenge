from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum, auto
from typing import Protocol

class PaymentService(Protocol):
    def process_payment(self, amount: Decimal) -> None:
        ...
    
    def process_payout(self, amount: Decimal) -> None:
        ...
        
class AccountType(StrEnum):
    SAVINGS = auto()
    CHECKING = auto()
    
@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: AccountType
    
    def deposit(self, amount: Decimal) -> None:
        print(
            f"Depositing {amount} into {self.account_type} Account {self.account_number}."
        )
        self.balance += amount
    
    def withdraw(self, amount: Decimal) -> None:
        if (self.balance - amount) > 0:
            print(
                f"Withdrawing {amount} from {self.account_type} Account {self.account_number}."
            )
            self.balance -= amount
        else:
            print(f"Sorry, not enough money in {self.account_type} Account to withdraw {amount}")
            
def deposit(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payment(amount)
    account.deposit(amount)
    
def withdraw(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payout(amount)
    account.withdraw(amount)
