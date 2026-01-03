import random

level = 1
score = 0

print("🔢 Welcome to the Number Guessing Game!")

while True:
    print(f"\n🎯 Level {level}")
    range_max = level * 5  # Increase difficulty each level
    secret = random.randint(1, range_max)
    attempts = 3

    print(f"I'm thinking of a number between 1 and {range_max}. You have {attempts} tries.")

    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess == secret:
            print("✅ Correct! You level up!")
            score += 10
            level += 1
            break
        elif guess < secret:
            print("📉 Too low!")
        else:
            print("📈 Too high!")
        
        attempts -= 1

    if attempts == 0:
        print(f"💀 Game Over! The number was {secret}.")
        print(f"Your final level: {level}, Score: {score}")
        break

    cont = input("Continue to next level? (yes/no): ").lower()
    if cont != 'yes':
        print(f"👋 Exiting game. Final level: {level}, Score: {score}")
        break
