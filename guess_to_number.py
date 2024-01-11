import turtle
import random

# Function to generate a random color
def generate_random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    return (red, green, blue)

# Function to display the RGB values
def display_rgb_values(rgb):
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("black")
    turtle.write(f"RGB: {rgb}", align="center", font=("Arial", 16, "normal"))

# Main game loop
def guess_the_color():
    turtle.speed(0)
    turtle.title("Guess the Color Game")

    while True:
        # Generate a random color
        color = generate_random_color()
        display_rgb_values(color)

        # Ask for user's guess
        guess = turtle.textinput("Guess the Color", "Enter RGB values (comma-separated):")

        # Check if the user wants to quit
        if guess is None:
            break

        # Convert the guess to a tuple of floats
        try:
            user_guess = tuple(float(x.strip()) for x in guess.split(","))
        except ValueError:
            print("Invalid input. Please enter three comma-separated numbers.")
            continue

        # Check if the user's guess matches the color
        if user_guess == color:
            turtle.clear()
            turtle.color(color)
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0, -50)
            turtle.color("white")
            turtle.write("Congratulations!", align="center", font=("Arial", 16, "normal"))
            turtle.goto(0, -80)
            turtle.write("Click to play again.", align="center", font=("Arial", 12, "normal"))
            turtle.exitonclick()
        else:
            print("Wrong guess. Try again!")

if __name__ == "__main__":
    guess_the_color()
