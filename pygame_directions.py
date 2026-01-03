import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_PATH = os.path.join(BASE_DIR, "Drums")

def playsound(yaw, pitch, roll):

    if -45 <= yaw <= -15:
        bass_drum = pygame.mixer.Sound(f"{DIR_PATH}/ryan_left.wav")
        bass_drum.play()
    if 15<= yaw <=45:
        classic =  pygame.mixer.Sound(f"{DIR_PATH}/ryan_right.wav")
        classic.play()
    if 15<= pitch <=40:
        drum_sound = pygame.mixer.Sound(f"{DIR_PATH}/ryan_up.wav")
        drum_sound.play()
    if -40<=pitch <=-15:
        drum_joke = pygame.mixer.Sound(f"{DIR_PATH}/ryan_down.wav")
        drum_joke.play()


def drum_sounds(yaw, pitch, roll):

    if -45 <= yaw <= -15:
        bass_drum = pygame.mixer.Sound(f"{DIR_PATH}/drum-joke-beat.wav")
        bass_drum.play()
    if 15<= yaw <=45:
        classic =  pygame.mixer.Sound(f"{DIR_PATH}/snare-drum-sound.wav")
        classic.play()
    if 15<= pitch <=40:
        drum_sound = pygame.mixer.Sound(f"{DIR_PATH}/classic.wav")
        drum_sound.play()
    if -40<=pitch <=-15:
        drum_joke = pygame.mixer.Sound(f"{DIR_PATH}/bass-drum.wav")
        drum_joke.play()

