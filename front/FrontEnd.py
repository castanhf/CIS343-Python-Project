import curses
import curses.textpad
import os
import sys

class FrontEnd:

    # default constructor
    def __init__(self, player, library):
        self.player = player
        self.library = library
     #   self.player.play(sys.argv[1])
        curses.wrapper(self.menu)

    # method responsible for menu window
    def menu(self, args):
        self.stdscr = curses.initscr()
        height,width = self.stdscr.getmaxyx()
        self.stdscr.addstr(1,10, "height: " + str(height))
        self.stdscr.addstr(2,10, "width: " + str(width))
        if height < 10 or width < 10:
            raise CLI_Audio_Screen_Size_Exception()
            return
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'): # This works but nothing happens on screen atm
                self.updateLibrary()
                self.stdscr.touchwin()
                self.stdscr.refresh()

    # This method is responsible for the library/playlist
    def updateLibrary(self):
        libWindow = curses.newwin(5, 70, 16, 5)
        libWindow.border()
        libWindow.addstr(0,0, 'New playlist? "y" for yes, "n" for no', curses.A_REVERSE)
        #libWindow.addstr(1,0, "Current playlist: " + self.library.my_media + "\n")
        libWindow.refresh()
        d = libWindow.getch()
        del libWindow
        if d == 27:
            self.quit()
        elif d == ord('y'):
            # a new playlist/library will be created/fetched
            # code is similar to changeSong() method
            # However it is not working - meaning the newwin
            # does not show up
            tempLibrary = curses.newwin(5, 40, 5, 50)
            tempLibrary.border()
            tempLibrary.addstr(0,0, 'What is the playlist path?', curses.A_REVERSE)
            self.stdscr.refresh()
            curses.echo()
            self.library.my_media = tempLibrary.getstr(1,1, 30)
            curses.noecho()
            self.library.createMedia()
            del tempLibrary
            self.stdscr.addstr(22,25, "                                    ")
            self.stdscr.addstr(22,25, "" + self.library.print_playlist())
            #self.library.playlistOK()
            youOk = curses.newwin(5, 40, 5, 50)
            youOk.border()
            youOk.addstr(0,0, 'Is this playlist ok? ("y" or "n")', curses.A_REVERSE)
            self.stdscr.refresh()
            e = youOk.getch()
            del youOk
            if e == 27:
                self.quit()
            elif e == ord('y'):
                self.stdscr.addstr(7, 35, 'Awesome!')
            elif e == ord('n'):
                self.stdscr.addstr(7, 35, 'You will have to enjoy it anyway')
        elif d == ord('n'):
            self.stdscr.addstr(22,25, "                                    ")
            self.stdscr.addstr(22,25, "" + self.library.print_playlist())
            #self.library.playlistOK()
            youOk2 = curses.newwin(5, 40, 5, 50)
            youOk2.border()
            youOk2.addstr(0,0, 'Is this playlist ok? ("y" or "n")', curses.A_REVERSE)
            self.stdscr.refresh()
            f = youOk2.getch()
            del youOk2
            if f == 27:
                self.quit()
            elif f == ord('y'):
                self.stdscr.addstr(7, 35, 'Awesome!')
            elif f == ord('n'):
                self.stdscr.addstr(7, 35, 'You will have to enjoy it anyway')
    
    # This method shows the song that is currently being played
    def updateSong(self):
        self.stdscr.addstr(15,10, '                                           ')
        self.stdscr.addstr(15,10, 'Now playing: ' + self.player.getCurrentSong())

    # This method changes the song that was currently playing into
    # another one that the user's desires to listen
    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, 'What is the file path?', curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        getPath = os.getcwd()+path
        fp = open(getPath, 'r+')
        if fp == None:
            raise CLI_Audio_File_Exception()
            return
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        self.player.play(path.decode(encoding="utf-8"))
        
    # quits the program
    def quit(self):
        self.player.stop()
        exit()
