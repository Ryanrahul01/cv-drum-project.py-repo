from os import environ
environ["PYGAME_HIDE__SUPPORT_PROMPT"] = '1'
import pygame, sys, time

#Initializing the mixer  
pygame.mixer.init()

#Load the music into the pygame memory so it can be played.
pygame.mixer.music.load('/Users/ryanrahul/Downloads/practice_drum_sound.mp3')

#Play the music and the loops is the amount of time that the audio is played. ex: input+1
#start is where user wants song to start, fade_ms is audio level increases by number of miliseconds
pygame.mixer.music.play(loops=1, start=0, fade_ms=2000)

input("Enter to exit")