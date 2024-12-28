import os.path
import pygame
import UserHandling
import OpenData # Class that opens files
from App.FunFacts import FunFacts


class MenuSetUp:

    def __init__(self, title, background_color):
        pygame.init()
        pygame.font.init()
        self.title = title
        self.background_color = background_color
        self.displaysurface = pygame.display.set_mode((500, 500))
        self.titlefont = pygame.font.SysFont('opensans', 64)
        self.contentfont = pygame.font.SysFont('opensans', 20)
        self.running = True

    def writeToScreen(self, text: str, posx: int, posy: int):
        text = self.contentfont.render(text, 1, (0, 0, 0))
        dest = text.get_rect(x=posx, y=posy)
        self.displaysurface.blit(text, dest)

    def drivemenu(self):
        self.displaysurface.fill(self.background_color)
        pygame.display.set_caption(self.title)

    def writetotopcentre(self, text):
        text = self.titlefont.render(text, 1, (0, 0, 0))
        dest = text.get_rect(center=(250, 30))
        self.displaysurface.blit(text, dest)


class SignIn(MenuSetUp):

    def __init__(self):
        super().__init__("Sign In", (250, 250, 250))
        self.password_rect = pygame.Rect(175, 300, 150, 50)
        self.signin_button_rect = pygame.Rect(200, 400, 100, 50)
        self.password = ""
        self.active = False

    def draw_signin_screen(self):
        self.displaysurface.fill(self.background_color)
        pygame.draw.rect(self.displaysurface, (100, 0, 0), self.password_rect, 2)
        display_text = '*' * len(self.password)
        text_surface = self.contentfont.render(display_text, True, (0, 0, 0))
        self.displaysurface.blit(text_surface, (self.password_rect.x + 5, self.password_rect.y + 15))
        pygame.draw.rect(self.displaysurface, (0, 0, 0), self.signin_button_rect)
        signin_text = self.contentfont.render("Sign In", True, (255, 255, 255))
        self.displaysurface.blit(signin_text, (self.signin_button_rect.x + 30, self.signin_button_rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.password_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.password = self.password[:-1]
                pygame.display.flip()
            if event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.password = ""
            elif event.key != pygame.K_RETURN:
                self.password += event.unicode


class DashBoard(MenuSetUp):

    def __init__(self):
        self.leftarrow = pygame.transform.scale(pygame.image.load(os.path.join("leftarrow.png")), (100, 100))
        self.rightarrow_img = pygame.transform.rotate(self.leftarrow, 180)
        super().__init__("DashBoard", (255, 255, 255))
        self.left_button_rect = pygame.Rect(50, 370, 150, 60)
        self.right_button_rect = pygame.Rect(300, 370, 150, 60)
        self.current_message = ""

    def clickleft(self):
        pygame.draw.rect(self.displaysurface, self.background_color, self.left_button_rect)
        self.displaysurface.blit(self.leftarrow, (50, 350))

    def clickright(self):
        pygame.draw.rect(self.displaysurface, self.background_color, self.right_button_rect)
        self.displaysurface.blit(self.rightarrow_img, (350, 350))

    def funfactsarea(self):
        pygame.draw.rect(self.displaysurface, (0, 0, 0), pygame.Rect(50, 150, 400, 200), 2)
        self.writeToScreen(self.current_message, 60, 160)


if __name__ == '__main__':
    current_screen = "SignIn"
    sign_in_screen = SignIn()
    dashboard_screen = DashBoard()
    Accounts = UserHandling.UserHandling()
    Facts = FunFacts()

    while True:
        if current_screen == "SignIn":
            sign_in_screen.drivemenu()
            sign_in_screen.draw_signin_screen()
            sign_in_screen.writetotopcentre("BlueBells")
            sign_in_screen.writeToScreen("Password: ", 100, 320)
        elif current_screen == "DashBoard":
            dashboard_screen.drivemenu()
            dashboard_screen.funfactsarea()
            dashboard_screen.clickleft()
            dashboard_screen.clickright()
            dashboard_screen.writetotopcentre("dashboard")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if current_screen == "SignIn":
                sign_in_screen.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN and sign_in_screen.signin_button_rect.collidepoint(event.pos):
                    password = sign_in_screen.password
                    Accounts.calchash(password)
                    if Accounts.checkhash():
                        current_screen = "DashBoard"

            if current_screen == "DashBoard":
                if event.type == pygame.MOUSEBUTTONDOWN and dashboard_screen.left_button_rect.collidepoint(event.pos):
                    dashboard_screen.current_message = "Left button clicked!"
                if event.type == pygame.MOUSEBUTTONDOWN and dashboard_screen.right_button_rect.collidepoint(event.pos):
                    dashboard_screen.current_message = "Right button clicked!"

        pygame.display.flip()
