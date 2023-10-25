answer = 11

def high_low(min: int, max: int, guess: int):
    global answer
    print(f"guessing {guess}")
    if guess == answer:
        # terminating condition
        print(f"found {answer}!")
        return

    if guess < answer:
        min = guess
    else:
        max = guess

    guess = (min + max) // 2
    high_low(min, max, guess)


high_low(0, 100, 50)