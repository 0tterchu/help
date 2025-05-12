import pygame
import os
import sys

# Initialize Pygame
pygame.init()
size = width, height = 480, 360
choice = input('Enter 1 (Save Position) or 2 (Spectator Mode): ')
screen = pygame.display.set_mode(size)

# Initialize position variables
if os.path.exists("pos.txt"):  # Check if the file exists
    with open("pos.txt", 'r') as f:
        lines = f.readlines()
        if len(lines) >= 2:  # Ensure there are at least two lines
            try:
                x, y = int(lines[0].strip()), int(lines[1].strip())  # Convert to integers
                print(x, y)
            except ValueError:
                print("Error: pos.txt contains invalid data. Defaulting to (0, 0).")
                x, y = 0, 0
        else:
            print("Error: pos.txt does not contain sufficient data. Defaulting to (0, 0).")
            x, y = 0, 0
else:
    print("Error: pos.txt file not found. Defaulting to (0, 0).")
    x, y = 0, 0

# Ensure choice is valid
if choice not in ['1', '2']:
    print("Invalid choice. Please enter '1' or '2'.")
    sys.exit()

print('start?')
input()
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if choice == '1':  # Save the position to a file
        with open("pos.txt", "w") as f:
            f.write(f"{x}\n{y}\n")  # Write the position on separate lines

    elif choice == '2':  # Spectator mode
        print('Spectator mode active.')
        pygame.time.wait(1000)  # Wait 1 second to avoid spamming the console

    # Update the game display
    screen.fill((0, 0, 0))  # Clear the screen with a black background
    pygame.display.update()

# Quit Pygame
pygame.quit()
