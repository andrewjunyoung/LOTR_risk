from random import randint

def get_stats(iterations, a_units=10, b_units=10):
    attacker_wins = 0
    defender_wins = 0

    for i in range(iterations):
        attacker_units_left, _ = battle(a_units, b_units)
        if attacker_units_left == 0: # Defender won
            defender_wins += 1
        else:
            attacker_wins += 1

    print(attacker_wins, defender_wins)
    print("Attacker win rate:", attacker_wins / (attacker_wins + defender_wins))

def battle(attackers, defenders,
        a_has_leader=False,
        b_has_leader=False,
        is_stronghold=False,
    ):
    while attackers > 0 and defenders > 0:
        attackers_sent = 3 if (attackers >= 3) else attackers
        defenders_sent = 2 if (defenders >= 2) else defenders

        attackers -= attackers_sent
        defenders -= defenders_sent

        # Do battle.
        attackers_returned, defenders_returned = battle_once(
            attackers_sent, defenders_sent
        )
        print("Sent:", attackers_sent, defenders_sent)
        print("Returned:", attackers_returned, defenders_returned)

        attackers += attackers_returned
        defenders += defenders_returned

        print("Now:", attackers, defenders)

    if attackers == 0:
        print(f"Defender wins with {defenders} units left.")
    else:
        print(f"Attacker wins with {attackers} units left.")

    return attackers, defenders

def battle_once(
        attacker, defender,
        a_has_leader=False,
        b_has_leader=False,
        is_stronghold=False
    ):
    attacker_rolls = roll_dice(attacker)
    defender_rolls = roll_dice(defender)

    if a_has_leader:
        attacker_rolls[0] += 1
    if b_has_leader:
        defender_rolls[0] += 1
    if is_stronghold:
        defender_rolls[0] += 1

    winner = get_winner(attacker_rolls, defender_rolls)

    if winner == "attacker":
        defender -= 1
    elif winner == "defender":
        attacker -= 1
    else:
        # something has gone horribly wrong
        raise Exception()

    return attacker, defender

def roll_dice(n_iterations):
    rolls = [randint(1, 6) for i in range(n_iterations)]
    rolls.sort(reverse=True)
    return rolls

def get_winner(attacker_rolls, defender_rolls):
    for i, defender_roll in enumerate(defender_rolls):
        try:
            attacker_roll = attacker_rolls[i]
        except:
            return "defender"

        if defender_roll > attacker_roll:
            return "defender"
        elif defender_roll < attacker_roll:
            return "attacker"
        else:  # The two rolls are equal
            continue

    # If all dice are equal, the defender wins.
    return "defender"
