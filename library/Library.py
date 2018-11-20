import os

class Library:
    my_media = (r"/home/castanhf/CIS343/projectPython/cli-audio/library/my_media/")

#    allMedia = []
    playlist = []

    # This method will search the defined directory and 
    # make a playlist
    def createMedia():
        for path, subdirs, files in os.walk(my_media):
            for file in files:
                if file.lower().endswith(('.wav')):
                    playlist.append(os.path.join(path, file))

    # This method will print the current playlist
    def print_playlist():
        print('\n - - - Playlist - - -\n')
        print('[{0}]'.format('\n - - - - - - - - - \n'.join(str(i) for i in enumerate(playlist, 1))))

    # This method will ask the user if the playlist is up to his/hers
    # preferences
    def playlistOK():
        ok = input('Is this playlist ok? ("yes" or "no")\n').lower()
        if ok == 'yes' or ok == 'y':
#            playPlaylist()
        elif ok == 'no' or ok == 'n':
            print("So sorry, but you will have to enjoy it ahah")
