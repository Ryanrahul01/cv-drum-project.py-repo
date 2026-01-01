import pygame, sys

pygame.mixer.init()

print("a = drum roll")
print("b = classic drum sound")
print("c = snare-drum-sound")
print("d = drum-joke-beat")
print('e = bass drum')
print("x = exit")

while True:
    user_input = input("Selected Key: ")

    if user_input == 'a':
        sound = pygame.mixer.Sound("/Users/ryanrahul/Downloads/drumroll.wav")
        sound.play()
    if user_input == 'b':
       classic =  pygame.mixer.Sound("/Users/ryanrahul/Downloads/classic.wav")
       classic.play()
    if user_input == 'c':
        drum_sound = pygame.mixer.Sound("/Users/ryanrahul/Downloads/snare-drum-sound.wav")
        drum_sound.play()
    if user_input == 'd':
       drum_joke = pygame.mixer.Sound("/Users/ryanrahul/Downloads/drum-joke-beat.wav")
       drum_joke.play()

    if user_input == 'e':
        bass_drum = pygame.mixer.Sound("/Users/ryanrahul/Downloads/bass-drum.wav")
        bass_drum.play()

    if user_input == 'x':
        sys.exit()
    