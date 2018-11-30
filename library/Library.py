import os

class Library:
   # my_media = (r"/home/castanhf/CIS343/projectPython/cli-audio/media/playlistTemp") # It only needs the .wav files inside the playlistTemp directory

#    allMedia = []
#    playlist = []

    def __init__(self):
        self.my_media = (r"/home/castanhf/CIS343/projectPython/cli-audio/media/playlistTemp")
        self.playlist = []
    
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
        return '\n - - - Playlist - - -\n[{0}]'.format('\n - - - - - - - - - \n'.join(str(i) for i in enumerate(self.playlist, 1)))
