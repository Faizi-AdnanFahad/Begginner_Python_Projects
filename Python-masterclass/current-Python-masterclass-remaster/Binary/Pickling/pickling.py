import pickle

# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((2, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open("imelda.pickle", "wb") as pickle_files:
#     pickle.dump(imelda, pickle_files)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    truck_number, track_title = track
    print(truck_number, track_title)