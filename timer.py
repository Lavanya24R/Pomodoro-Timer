import pygame
import sys
import requests
import webbrowser
from button import Button

pygame.init()

WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")

CLOCK = pygame.time.Clock()

BACKDROP = pygame.image.load("image_assets/backdrop.png")
WHITE_BUTTON = pygame.image.load("image_assets/button.png")

FONT = pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2-80, HEIGHT/2-15))

START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START",
                    pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro",
                    pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break",
                    pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break",
                    pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")

POMODORO_LENGTH = 7200 # 7200 secs / 2 hrs
SHORT_BREAK_LENGTH = 600 # 600 secs / 10 mins
LONG_BREAK_LENGTH = 1800 # 1800 secs / 1 hrs

current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                started = not started
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False
            START_STOP_BUTTON.text_input = "STOP" if started else "START"
            START_STOP_BUTTON.text = pygame.font.Font("image_assets/ArialRoundedMTBold.ttf", 20).render(
                START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1

    SCREEN.fill("#ba4949")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))
    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
        display_hrs=int(current_seconds/3600)
    else:
        # Make an HTTP request to the Flask server to redirect to the HTML page
        print("Timer ended, making HTTP request to /end") 
        response = requests.get("http://127.0.0.1:5000/end") 
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200: 
            # Open the HTML page in the default web browser 
            webbrowser.open("http://127.0.0.1:5000/end")
        pygame.quit()
        sys.exit()
    timer_text = FONT.render(f"{display_hrs:02}:{display_minutes:02}:{display_seconds:02}", True, "white")
    SCREEN.blit(timer_text, timer_text_rect)

    pygame.display.update()
