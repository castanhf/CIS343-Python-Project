import os

class Library:
   # my_media = (r"/home/castanhf/CIS343/projectPython/cli-audio/media/playlistTemp") # It only needs the .wav files inside the playlistTemp directory

#    allMedia = []
#    playlist = []

    def __init__(self):
        self.my_media = (r"/home/castanhf/CIS343/projectPython/cli-audio/media/playlistTemp")
        playlist = []
    
    # This method will search the defined directory and 
    # make a playlist
    def createMedia(self):
        print(self.my_media);
        for path, subdirs, files in os.walk(my_media):
            for file in files:
                if file.lower().endswith(('.wav')):
                    playlist.append(os.path.join(path, file))

    # This method will print the current playlist
    def print_playlist(self):
        print('\n - - - Playlist - - -\n')
        print('[{0}]'.format('\n - - - - - - - - - \n'.join(str(i) for i in enumerate(playlist, 1))))

    # This method will ask the user if the playlist is up to his/hers
    # preferences
    def playlistOK(self):
        ok = input('Is this playlist ok? ("y" or "n")\n').lower()
        if ok == ord('y'):
            print("Awesome!")
        elif ok == ord('n'):
            print("So sorry, but you will have to enjoy it ahah")
