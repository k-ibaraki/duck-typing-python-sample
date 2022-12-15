# 抽象基底クラス(ABC)サンプル
# 人間である→絵が描ける

from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class Tanaka(Human):
    def draw(self) -> None:
        print("😁")


class Yamada(Human):
    def draw(self) -> None:
        print("👶")


class Suzuki(Human):
    def write(self) -> None:
        print("こんにちは")


class AI:
    def draw(self) -> None:
        print("👽")


def run_draw(human: Human) -> None:
    human.draw()


tanaka: Tanaka = Tanaka()
yamada: Yamada = Yamada()
# suzuki: Suzuki = Suzuki()
ai: AI = AI()

run_draw(tanaka)
run_draw(yamada)
# run_draw(ai)
