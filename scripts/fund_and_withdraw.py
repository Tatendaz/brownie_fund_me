from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"Current contract balance is {fund_me.balance()}")


def withdraw():
    print("Running withdraw function")
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print(f"Current contract balance is {fund_me.balance()}")


def main():
    fund()
    withdraw()
