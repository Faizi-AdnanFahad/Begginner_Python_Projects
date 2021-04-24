# # Creating a binary file
# with open("binary", 'bw') as bin_files:
#     for i in range(17):
#         bin_files.write(bytes([i]))  # returning i integer as byte object
#
# # Printing binary files in the console
# with open("binary", 'br') as binFiles:
#     for b in binFiles:
#         print(b)


a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
d = 2998302     # 00 2D C0 1E

with open("binary2", "bw") as bin_files:
    bin_files.write(a.to_bytes(2, "big"))
    bin_files.write(a.to_bytes(2, "big"))
    bin_files.write(a.to_bytes(4, "big"))
    bin_files.write(a.to_bytes(4, "big"))
    bin_files.write(a.to_bytes(4, "little"))


with open("binary2", "br") as bin_files:
    e = int.from_bytes(bin_files.read(2), "big")
    print(e)
    f = int.from_bytes(bin_files.read(2), "big")
    print(f)
    g = int.from_bytes(bin_files.read(4), "big")
    print(g)
    h = int.from_bytes(bin_files.read(4), "big")
    print(h)
    i = int.from_bytes(bin_files.read(4), "big")
    print(i)
















