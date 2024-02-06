from tkinter import *
import random

gameWidth = 750
gameHeight = 750
spedUpSnake = 100
snakeSpeed = 250
normalSnakeSpeed = 250
objectsSized = 50
bodyParts = 3
snakeColor = "#00FF00"       # Green
appleColor = "#FF0000"       # Red
playgroundColor = "#000000"  # Black


class Snake:

    def __init__(self):
        self.bodySize = bodyParts
        self.coordinates = []
        self.squares = []

        for i in range(0, bodyParts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + objectsSized, y + objectsSized, fill=snakeColor, tag="snake")
            self.squares.append(square)


class Apple:

    def __init__(self):

        x = random.randint(0, int(gameWidth/objectsSized - 1))* objectsSized
        y = random.randint(0, int(gameHeight/objectsSized - 1))* objectsSized

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + objectsSized, y + objectsSized, fill=appleColor, tag="Apple")


def movements(snake,apple):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= objectsSized
    elif direction == "down":
        y += objectsSized
    elif direction == "left":
        x -= objectsSized
    elif direction == "right":
        x += objectsSized

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle (x, y, x + objectsSized, y+ objectsSized, fill=snakeColor)

    snake.squares.insert(0, square)

    if x == apple.coordinates[0] and y == apple.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("Apple")

        apple = Apple()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if checkCollisions(snake):
        gameOver()

    else:
        window.after(snakeSpeed, movements, snake, apple)


def changeDirectionLeft(event):
    changeDirection('left')

def changeDirectionRight(event):
    changeDirection('right')

def changeDirectionUp(event):
    changeDirection('up')

def changeDirectionDown(event):
    changeDirection('down')

def changeDirection(newDirection):

    global direction

    if newDirection == 'left':
        if direction != 'right':
            direction = newDirection
    elif newDirection == 'right':
        if direction != 'left':
            direction = newDirection
    elif newDirection == 'up':
        if direction != 'down':
            direction = newDirection
    elif newDirection == 'down':
        if direction != 'up':
            direction = newDirection

def checkCollisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= gameWidth:
        return True
    elif y < 0 or y >= gameHeight:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def gameOver():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                    font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

def on_key_pressUp(event):
    global consecutive_key_pressesUp
    global snakeSpeed

    consecutive_key_pressesUp += 1
    snakeSpeed = normalSnakeSpeed

    if consecutive_key_pressesUp >= 3:
        consecutive_key_pressesUp = 0
        snakeSpeed = spedUpSnake
        reset_counter()

def on_key_pressLeft(event):
    global consecutive_key_pressesLeft
    global snakeSpeed

    consecutive_key_pressesLeft += 1
    snakeSpeed = normalSnakeSpeed

    if consecutive_key_pressesLeft >= 3:
        consecutive_key_pressesLeft = 0
        snakeSpeed = spedUpSnake
        reset_counter()

def on_key_pressRight(event):
    global consecutive_key_pressesRight
    global snakeSpeed

    consecutive_key_pressesRight += 1
    snakeSpeed = normalSnakeSpeed

    if consecutive_key_pressesRight >= 3:
        consecutive_key_pressesRight = 0
        snakeSpeed = spedUpSnake
        reset_counter()


def on_key_pressDown(event):
    global consecutive_key_pressesDown
    global snakeSpeed

    consecutive_key_pressesDown += 1
    snakeSpeed = normalSnakeSpeed

    if consecutive_key_pressesDown >= 3:
        consecutive_key_pressesDown = 0
        snakeSpeed = spedUpSnake
        reset_counter()

def on_key_release(event):
    global consecutive_key_presses
    global snakeSpeed

    consecutive_key_presses = 0
    snakeSpeed = normalSnakeSpeed

def mixleft(event):


    changeDirectionLeft(event)
    on_key_pressLeft(event)

def mixRight(event):

    changeDirectionRight(event)
    on_key_pressRight(event)

def mixUp(event):


    changeDirectionUp(event)
    on_key_pressUp(event)

def mixDown(event):


    changeDirectionDown(event)
    on_key_pressDown(event)

def reset_counter():
    global consecutive_key_pressesUp 
    global consecutive_key_pressesDown 
    global consecutive_key_pressesRight 
    global consecutive_key_pressesLeft 
    consecutive_key_pressesUp = 0
    consecutive_key_pressesDown = 0
    consecutive_key_pressesRight = 0
    consecutive_key_pressesLeft = 0

window = Tk()
window.title("Snake game!")
window.resizable(False,False)

score = 0
direction = 'down'
consecutive_key_pressesUp = 0
consecutive_key_pressesDown = 0
consecutive_key_pressesRight = 0
consecutive_key_pressesLeft = 0

label = Label(window, text=f"Score : {score}", font=("Arial", 50))
label.pack()

canvas = Canvas(window, bg=playgroundColor, height=gameHeight, width=gameWidth)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', mixleft)
window.bind('<Right>', mixRight)
window.bind('<Up>', mixUp)
window.bind('<Down>', mixDown)


snake = Snake()
apple = Apple()

movements(snake, apple)

window.mainloop()
