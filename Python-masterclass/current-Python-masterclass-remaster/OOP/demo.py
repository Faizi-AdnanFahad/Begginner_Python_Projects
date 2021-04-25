a_string = "this is\na string split\t\tand tabbed"
print(a_string)  # a string split		and tabbed

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)  # this is\na string split\t\tand tabbed

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
