import os.path
import pygame
import UserHandling
from App.UserHandling import Userhandling


class MenuSetUp:

    def __init__(self, title, background_color):
        pygame.init()  # Initialize Pygame
        pygame.font.init()  # Get the fonts
        self.title = title  # Title parameter passed
        self.background_color = background_color  # Set background color
        self.displaysurface = pygame.display.set_mode((500, 500))  # Tuple for window size
        self.titlefont = pygame.font.SysFont('opensans', 64)
        self.contentfont = pygame.font.SysFont('opensans', 16)
        self.running = True  # Running so it can be stopped

    def drivemenu(self):
        self.displaysurface.fill(self.background_color)  # Put background color on the screen
        pygame.display.set_caption(self.title)  # Put caption in top left corner

    def writetotopcentre(self, text):
        text = self.titlefont.render(text, 1, (0, 0, 0))
        dest = text.get_rect(center=(250, 30))  # All screens are same size
        self.displaysurface.blit(text, dest)


class SignIn(MenuSetUp):  # SignIn screen
    def __init__(self):
        super().__init__("Sign In", (250, 250, 250))
        self.password_rect = pygame.Rect(175, 300, 150, 50)  # Password input rectangle
        self.signin_button_rect = pygame.Rect(200, 400, 100, 50)  # Sign-in button rectangle
        self.password = ""  # Store the password entered by the user
        self.active = False  # Track if the password input box is active for input

    def draw_signin_screen(self):
        # Fill background
        self.displaysurface.fill(self.background_color)

        # Draw the password rectangle (input box)
        pygame.draw.rect(self.displaysurface, (100, 0, 0), self.password_rect, 2)

        # Display the password as asterisks
        display_text = '*' * len(self.password)  # Replace characters with asterisks
        text_surface = self.contentfont.render(display_text, True, (0, 0, 0))
        self.displaysurface.blit(text_surface, (self.password_rect.x + 5, self.password_rect.y + 15))

        # Draw the sign-in button
        pygame.draw.rect(self.displaysurface, (0, 0, 0), self.signin_button_rect)
        signin_text = self.contentfont.render("Sign In", True, (255, 255, 255))
        self.displaysurface.blit(signin_text, (self.signin_button_rect.x + 30, self.signin_button_rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the password input box is clicked
            if self.password_rect.collidepoint(event.pos):
                self.active = True  # Activate the input box
            else:
                self.active = False  # Deactivate if clicked outside

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                # Remove the last character
                self.password = self.password[:-1]
            if event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.password = ""
            else:
                # Add character to the password
                self.password += event.unicode


class DashBoard(MenuSetUp):  # Dashboard screen
    def __init__(self):
        self.leftarrow = pygame.transform.scale(pygame.image.load(os.path.join("leftarrow.png")), (100, 100))
        self.rightarrow_img = pygame.transform.rotate(self.leftarrow, 180)  # Right is left rotated 180 degrees

        super().__init__("DashBoard", (255, 255, 255))  # Set the color using hex values here

        # Define button rectangles for left and right buttons
        self.left_button_rect = pygame.Rect(50, 370, 150, 60)  # Left button rectangle
        self.right_button_rect = pygame.Rect(300, 370, 150, 60)  # Right button rectangle

    def clickleft(self):
        # Draw left button and arrow
        pygame.draw.rect(self.displaysurface, self.background_color, self.left_button_rect)  # Draw the left button
        self.displaysurface.blit(self.leftarrow, (50, 350))  # Draw left arrow

    def clickright(self):
        # Draw right button and arrow
        pygame.draw.rect(self.displaysurface, self.background_color, self.right_button_rect)  # Draw the right button (green color)
        self.displaysurface.blit(self.rightarrow_img, (350, 350))  # Draw right arrow (rotated)

    def funfactsarea(self):
        pygame.draw.rect(self.displaysurface, (0, 0, 0), pygame.Rect(50, 150, 400, 200), 2)  # Fun facts area


# Initialize state and screens
current_screen = "SignIn"  # Start with sign-in screen
sign_in_screen = SignIn()  # Create instance of sign-in
dashboard_screen = DashBoard()  # Create instance of dashboard

while True:
    # Allows for screen swap but still using MenuSetUp
    if current_screen == "SignIn":
        sign_in_screen.drivemenu()
        sign_in_screen.draw_signin_screen()
    elif current_screen == "DashBoard":
        dashboard_screen.drivemenu()
        dashboard_screen.funfactsarea()
        dashboard_screen.clickleft()
        dashboard_screen.clickright()
        dashboard_screen.writetotopcentre("dashboard")

    pygame.display.flip()  # Draw the screen

    for event in pygame.event.get():  # Exit on x pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Handle events for the sign-in screen
        if current_screen == "SignIn":
            sign_in_screen.handle_event(event)

            # Check if the user clicks the "Sign In" button
            if event.type == pygame.MOUSEBUTTONDOWN and sign_in_screen.signin_button_rect.collidepoint(event.pos):
                print("Sign-in successful!")
                print(f"Password entered: {sign_in_screen.password}")  # Use the password here
                print(Userhandling.calchash(sign_in_screen.password))
                current_screen = "DashBoard"  # Switch to the dashboard screen

        # Check if mouse clicked on the left or right button on the dashboard
        if current_screen == "DashBoard":
            if event.type == pygame.MOUSEBUTTONDOWN and dashboard_screen.left_button_rect.collidepoint(event.pos):
                print("Left button pressed")
            if event.type == pygame.MOUSEBUTTONDOWN and dashboard_screen.right_button_rect.collidepoint(event.pos):
                print("Right button pressed")
