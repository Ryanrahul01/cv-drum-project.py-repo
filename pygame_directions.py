import pygame, sys
def playsound(yaw, pitch, roll):

    if -45 <= yaw <= -15:
        bass_drum = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/left.wav")
        bass_drum.play()
    if 15<= yaw <=45:
        classic =  pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/right.wav")
        classic.play()
    if 15<= pitch <=40:
        drum_sound = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/up.wav")
        drum_sound.play()
    if -40<=pitch <=-15:
        drum_joke = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/down.wav")
        drum_joke.play()


def drum_sounds(yaw, pitch, roll):

    if -45 <= yaw <= -15:
        bass_drum = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/drum-joke-beat.wav")
        bass_drum.play()
    if 15<= yaw <=45:
        classic =  pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/snare-drum-sound.wav")
        classic.play()
    if 15<= pitch <=40:
        drum_sound = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/classic.wav")
        drum_sound.play()
    if -40<=pitch <=-15:
        drum_joke = pygame.mixer.Sound("/Users/ryanrahul/Documents/CV_ISEF_PROJECT/cv-gesture-sound/Drums/bass-drum.wav")
        drum_joke.play()

