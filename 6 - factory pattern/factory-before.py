from abc import ABC, abstractmethod
from typing import List

class Exchange(ABC):
    @abstractmethod
    def connect(self, user: str, password: str):
        pass

    def get_market_data(self, coin: str) -> List[float]:
        pass

class TradingBot(ABC):
    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

class CoinBase(Exchange):
    def connect(self, user: str, password: str):
        print(f"Connecting {user} to CoinBase...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 25, 5, 20]

class Binance(Exchange):
    def connect(self, user: str, password: str):
        print(f"Connecting {user} to Binance...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 25, 5, 20]


class Average(TradingBot):
    def list_average(self, list: List[float]) -> float:
        return sum(list) / len(list)

    def should_buy(self, prices: List[float]) -> bool:
        print(f"Average: {self.list_average(prices)}")
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

class MinMax(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)

class Application:

    exchange: Exchange
    bot: TradingBot

    def __init__(self, trading_setup = "risky"):
        if trading_setup == "risky":
            self.exchange = Binance()
            self.bot = Average()
        else:
            self.exchange = CoinBase()
            self.bot = Average()

    def connect(self):
        self.exchange.connect("Arjan", "BestPasswordEva")

    def check_prices(self, coin: str):
        prices = self.exchange.get_market_data("BTC/USD")
        should_buy = self.bot.should_buy(prices)
        should_sell = self.bot.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")

application = Application("cautious")
application.connect()
application.check_prices("BTC/USD")
