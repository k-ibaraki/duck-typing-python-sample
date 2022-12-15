# ダックタイピングサンプル(Protocol)
# 絵が描ける→人間である

from typing import Protocol

class Human(Protocol):
  def draw(self) -> None:
    ...

class Tanaka:
  def draw(self) -> None:
    print("😁")

class Yamada:
  def draw(self) -> None:
    print("👶")

class Suzuki:
  def write(self) -> None:
    print("こんにちは")

class AI:
  def draw(self) -> None:
    print("👽")

def run_draw(human: Human) -> None:
  human.draw()

yamada: Yamada = Yamada() # 正常
tanaka: Tanaka = Tanaka() # 正常

# 絵がかけなくてもインスタンスは作れる
suzuki: Suzuki = Suzuki() 

ai: AI = AI()

run_draw(yamada)
run_draw(tanaka)
# 鈴木は絵が描けないのrun_drawは実行出来ない
# run_draw(suzuki) 

# aiは絵が描けるので問題なし
run_draw(ai) 
