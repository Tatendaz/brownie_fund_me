from brownie import MockV3Aggregator, FundMe, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()

    # pass the price feed address to our fundme contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        publish = config["networks"][network.show_active()]["verify"]
    else:
        deploy_mocks(account)
        price_feed_address = MockV3Aggregator[-1].address
        publish = config["networks"][network.show_active()]["verify"]

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=publish,  # optionally we can set verify in the config file and pull from there
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
