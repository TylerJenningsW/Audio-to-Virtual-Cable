import win32gui
import keyboard
import pygame
import time
def main():
     pygame.mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
     pygame.mixer.music.load('beep12.ogg')
     pygame.mixer.music.set_volume(0.1)
     started = False
     start = "z"
     end = "x"
     while True:
          time.sleep(0.1)
          active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
          if started == False and keyboard.is_pressed(start) and active_window == 'Type to Voice Chat':
               started = True
               pygame.mixer.music.play()
               time.sleep(2)
               pygame.mixer.music.stop()
          if started == True and keyboard.is_pressed(end) and active_window == 'Type to Voice Chat':
               started = False
if __name__ == "__main__":
     main()