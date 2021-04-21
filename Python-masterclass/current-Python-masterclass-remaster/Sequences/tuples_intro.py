# t = ("a", "b", "c")
# print(t)

# Tuples are immutable

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

for album in albums:
    print(f"Album: {album[0]}, Artist: {album[1]}, Year: {album[2]}")
print()
# Unpacking 
for album in albums:
    album, artist, year = album
    print(f"Album: {album}, Artist: {artist}, Year: {year}")
print()
# Unpacking
for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")





# metallica = ("Ride the Lightning", "Metallica", 1984)
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# # Usefulness of tuple
#
# # 1. Can be confusing because numbers can be mixed;
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# # 2. easy to read because we know what each argument is representing by assigning it to a variable using unpacking.
# name, length, width, height, price = table
# print(length * width)
#
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
# #
# # metallica2 = list((metallica))
# # print(metallica2)
# #
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
