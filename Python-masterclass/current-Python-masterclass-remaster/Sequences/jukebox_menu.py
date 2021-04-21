from nested_data import albums

# First Solution - My Solution
# --------------
# while True:
#     print("Please choose your album (invalid choice exits): ")
#     for indexAlbum, album in enumerate(albums):
#         print(f"{indexAlbum + 1}: {album[0]}")
#
#     inputAlbum = int(input())
#     if 1 <= inputAlbum <= len(albums):
#         albumSongs = albums[inputAlbum - 1][3]
#         while True:
#             print("Please choose your song: ")
#             for numSong, songTitle in albumSongs:
#                 print(f"{numSong}: {songTitle}")
#
#             inputSong = int(input())
#             if 1 <= inputSong <= len(albumSongs):
#                 print(f"Playing {albumSongs[inputSong - 1][1]}")
#                 print(40 * "=")
#             else:
#                 break
#     else:
#         break

# Second Solution - Instructor
# --------------
SONGS_LIST_INDEX = 3  # Constant
SONG_TITLE_INDEX = 1  # Constant
while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}:  {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_List = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for track, song in song_List:
        print(f"{track}: {song}")

    song_choice = int(input())

    if 1 <= song_choice <= len(song_List):
        title = song_List[song_choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")

    print(40 * "=")


# OR
# for index, tuples in enumerate(albums):
#     title, artist, year, songs in tuples:






