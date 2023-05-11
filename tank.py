# Import pygame module
import pygame

# Initialize pygame
pygame.init()

# Create a screen with width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# Set the title and icon of the window
pygame.display.set_caption("Shoot Each Other")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Load the background image
background = pygame.image.load("background.png")

# Load the player 1 image and set its initial position and speed
player1 = pygame.image.load("player1.png")
player1_x = 100
player1_y = 300
player1_speed_x = 0
player1_speed_y = 0

# Load the player 2 image and set its initial position and speed
player2 = pygame.image.load("player2.png")
player2_x = 700
player2_y = 300
player2_speed_x = 0
player2_speed_y = 0

# Load the bullet image and set its initial position and speed
bullet = pygame.image.load("bullet.png")
bullet_x = -100
bullet_y = -100
bullet_speed_x = 0
bullet_speed_y = 0

# Load the tank image and set its initial position and speed
tank = pygame.image.load("tank.png")
tank_x = 400
tank_y = -100
tank_speed_y = 0.2

# Define a function to draw the player 1 on the screen
def draw_player1(x, y):
    screen.blit(player1, (x, y))

# Define a function to draw the player 2 on the screen
def draw_player2(x, y):
    screen.blit(player2, (x, y))

# Define a function to draw the bullet on the screen
def draw_bullet(x, y):
    screen.blit(bullet, (x, y))

# Define a function to draw the tank on the screen
def draw_tank(x, y):
    screen.blit(tank, (x, y))

# Define a function to check if the player and the bullet collide
def is_collision(player_x, player_y, bullet_x, bullet_y):
    # Calculate the distance between the centers of the player and the bullet
    distance = ((player_x - bullet_x) ** 2 + (player_y - bullet_y) ** 2) ** 0.5
    
    # If the distance is less than 50 pixels, return True (collision)
    if distance < 50:
        return True
    
    # Otherwise, return False (no collision)
    else:
        return False

# Define a function to check if the tank and the bullet collide
def is_tank_collision(tank_x, tank_y, bullet_x, bullet_y):
    # Calculate the distance between the centers of the tank and the bullet
    distance = ((tank_x - bullet_x) ** 2 + (tank_y - bullet_y) ** 2) ** 0.5
    
    # If the distance is less than 100 pixels, return True (collision)
    if distance < 100:
        return True
    
    # Otherwise, return False (no collision)
    else:
        return False

# Create a variable to store the game loop condition
running = True

# Start the game loop
while running:

    # Fill the screen with the background image
    screen.blit(background, (0, 0))

    # Check for any events (such as keyboard input or mouse click)
    for event in pygame.event.get():

        # If the event is quitting the game (such as clicking the X button), exit the loop
        if event.type == pygame.QUIT:
            running = False

        # If the event is pressing a key, change the player speed accordingly
        if event.type == pygame.KEYDOWN:
            # For player 1: use W, A, S, D keys to move and space key to shoot
            if event.key == pygame.K_w:
                player1_speed_y = -0.5
            if event.key == pygame.K_a:
                player1_speed_x = -0.5
            if event.key == pygame.K_s:
                player1_speed_y = 0.5
            if event.key == pygame.K_d:
                player1_speed_x = 0.5
            if event.key == pygame.K_SPACE:
                bullet_x = player1_x + 50 # Set the bullet position to be next to player 1's right side 
                bullet_y = player1_y + 25 # Set the bullet # position to be at player 1's center vertically 
                bullet_speed_x = 1 # Set the bullet speed to move rightward
            
            # For player 2: use arrow keys to move and enter key to shoot
            if event.key == pygame.K_UP:
                player2_speed_y = -0.5
            if event.key == pygame.K_LEFT:
                player2_speed_x = -0.5
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0.5
            if event.key == pygame.K_RIGHT:
                player2_speed_x = 0.5
            if event.key == pygame.K_RETURN:
                bullet_x = player2_x - 50 # Set the bullet position to be next to player 2's left side 
                bullet_y = player2_y + 25 # Set the bullet position to be at player 2's center vertically 
                bullet_speed_x = -1 # Set the bullet speed to move leftward
        
        # If the event is releasing a key, stop the player movement
        if event.type == pygame.KEYUP:
            # For player 1: use W, A, S, D keys to move and space key to shoot
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_speed_y = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1_speed_x = 0
            
            # For player 2: use arrow keys to move and enter key to shoot
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_speed_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2_speed_x = 0
    
    # Update the player 1 position based on the speed and the screen boundaries
    player1_x += player1_speed_x
    player1_y += player1_speed_y

    if player1_x < 0:
        player1_x = 0
    elif player1_x > 750:
        player1_x = 750
    
    if player1_y < 0:
        player1_y = 0
    elif player1_y > 550:
        player1_y = 550
    
    # Update the player 2 position based on the speed and the screen boundaries
    player2_x += player2_speed_x
    player2_y += player2_speed_y

    if player2_x < 0:
        player2_x = 0
    elif player2_x > 750:
        player2_x = 750
    
    if player2_y < 0:
        player2_y = 0
    elif player2_y > 550:
        player2_y = 550
    
    # Update the bullet position based on the speed and reset it if it goes off-screen
    bullet_x += bullet_speed_x

    if bullet_x < -100 or bullet_x > 800:
        bullet_x = -100
        bullet_speed_x = 0
    
    # Update the tank position based on the speed and reset it if it goes off-screen
    tank_y += tank_speed_y

    if tank_y > 600:
        tank_y = -100
    
    # Check if there is a collision between the bullet and either of the players
    collision1 = is_collision(player1_x, player1_y, bullet_x, bullet_y)
    collision2 = is_collision(player2_x, player2_y, bullet_x, bullet_y)

    # If there is a collision, end the game and display a message
    if collision1:
        running = False
        font = pygame.font.SysFont("arial", 64)
        text = font.render("Player 2 Wins", True, (255, 0, 0))
        screen.blit(text, (200, 250))
    
    if collision2:
        running = False
        font = pygame.font.SysFont("arial", 64)
        text = font.render("Player 1 Wins", True, (255, 0, 0))
        screen.blit(text, (200, 250))
    
    # Check if there is a collision between the tank and the bullet
    tank_collision = is_tank_collision(tank_x, tank_y, bullet_x, bullet_y)

    # If there is a collision, increase the tank speed and reset the bullet position
    if tank_collision:
        tank_speed_y += 0.1
        bullet_x = -100
        bullet_speed_x =
