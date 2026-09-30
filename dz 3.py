import random
def roll():
    return [random.randint(1, 6) for _ in range(6)]
def count(dice, v):
    return dice.count(v)
def player(current):
    while True:
        s = input("Ставка 'кол-во номинал' или 'верю'/'не верю': ").lower().split()
        if s[0] in ("верю", "не"):
            return " ".join(s), None
        c, v = int(s[0]), int(s[1])
        if 1 <= v <= 6 and c >= 1 and (current is None or (c, v) > current):
            return "ставка", (c, v)
        print("Плохая ставка!")
def comp(current, dice):
    if current is None:
        return "ставка", (1, random.randint(1, 6))
    c, v = current
    need = c - count(dice, v)
    if need > 3 and random.random() < 0.7:
        return "не верю", None
    if need <= 1 and random.random() < 0.4:
        return "верю", None
    if random.random() < 0.5:
        return "ставка", (c + 1, v)
    return "ставка", (c, v + 1) if v < 6 else (c + 1, 1)
def check(bid, all_dice, who):
    c, v = bid
    real = count(all_dice, v)
    print(f"\nЗаявлено {c} x {v}, реально {real}")
    print("Все кости:", all_dice)
    if real >= c:
        print(f"Ставка верна! {who} проиграл.")
    else:
        print(f"Ставка ложна! {who} проиграл.")
mine = roll()
enemy = roll()
print("Твои кости:", mine)
current = None
turn = "я"
while True:
    if turn == "я":
        act, bid = player(current)
        if act == "ставка":
            current = bid
            turn = "комп"
        elif act in ("верю", "не") and current:
            if act == "верю":
                turn = "комп"
            else:
                check(current, mine + enemy, "комп")
                break
    else:
        act, bid = comp(current, enemy)
        if act == "ставка":
            print("Комп ставит:", bid)
            current = bid
            turn = "я"
        elif act == "верю":
            print("Комп: верю")
            turn = "я"
        else:
            check(current, mine + enemy, "я")
            break
