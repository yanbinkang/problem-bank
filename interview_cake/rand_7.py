def rand7():

    while True:
        # do our die rolls
        roll1 = rand5()
        roll2 = rand5()

        outcome_number = (roll1-1) * 5 + (roll2-1) + 1

        # if we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # our outcome was fine. return it!
        return outcome_number % 7 + 1
