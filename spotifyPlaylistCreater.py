# author: Blake Nygren
# 1/9/21
#
# create spotify playlists based on command line argument
# includes Christmas and Halloween
# -------------------------------------------------------

import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

christmasSongs = [
"3tTpegNWYZFhkymRT2xhgF",
"0bYg9bo50gSsH3LtXe2SQn",
"6wn2nmFn3wDuiMldRiuRuL",
"1ADjWm8QNhgNV8yCNNgQ1T",
"5a1iz510sv2W9Dt1MvFd5R",
"2L9QLAhrvtP4EYg1lY0Tnw",
"5xlS0QkVrSH7ssEbBgBzbM",
"2pnPe4pJtq7689i5ydzvJJ",
"1XBc4r6ltXjkFJBrsttwIF",
"4cJhiux4xzrdgSHUeAjP48",
"1SV1fxF65n9NhRHp3KlBuu",
"1hvpDAxZPKjKztOc72sv06",
"2qoZNAP3JLyIOtbsPtBjvV",
"3nAp4IvdMPPWEH9uuXFFV5"
]
halloweenSongs = [
"0xxZY5C9xxij3D1HkzbnfC",
"23V08GxMeaZNSf8Gy6KF6t",
"3S2R0EVwBSAVMd5UMgKTL0",
"01YROQCnF1AQm7SCWJmD2o"
]

# if Christmas playlist selected
# create Christmas and add songs
def createPlaylist(which):

    #initialize Spotify credentials
    token = spotipy.util.prompt_for_user_token(username="blakemode777", 
    scope="playlist-modify-private",
    client_id="479e0dc981994aa1a4a4aa3acd25bdb7",
    client_secret="a5e15563e82f4af0898e03764ba821e9",
    redirect_uri="https://accounts.spotify.com/authorize",
    show_dialog=False
    )

    sp = spotipy.Spotify(auth=token)


    # TODO add descriptions to each playlist?
    if(which == "c"):
        playlistName = "Christmas!"
    else:
        playlistName = "Halloween!"
    
    # create playlist
    new = sp.user_playlist_create(user="blakemode777", name=playlistName, public=False)

    # add songs based on which playlist is being made
    # TODO can make this more efficient
    if(which == "c"):
        sp.user_playlist_add_tracks(user="blakemode777", playlist_id=new["id"], tracks=christmasSongs)       
    else:
        sp.user_playlist_add_tracks(user="blakemode777", playlist_id=new["id"], tracks=halloweenSongs)

def main():
   
    print("########## Spotify Playlist Creater ##########\n")

    # check command arg to find what action
    # should be taken
    if(len(sys.argv) > 1):
        cmdInput = str(sys.argv[1])
    else: 
        # print info if no cmd arg
        # handle input
        cmdInput = input("Which playlist would you like to create: ")

    # check for Christmas selected
    if(cmdInput.lower() == "c" or cmdInput.lower() == "christmas"):
        print("Creating Christmas Playlist...")
        createPlaylist("c")

    # check for Halloween selected
    elif(cmdInput.lower() == "h" or cmdInput.lower() == "halloween"):
        print("Creating Halloween Playlist...")
        createPlaylist("h")

    # no cmd line argument
    elif(cmdInput is None):
        pass
       
        
if __name__ == '__main__':
    main()