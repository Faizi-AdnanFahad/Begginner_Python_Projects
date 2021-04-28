

try:
    f = open('test.txt')
    temp_corrupt = open('Curropt_file')
    if temp_corrupt.name == 'Curropt_file.txt':
        raise Exception  # Raises the exception error - 3rd one
    # var = bad_var
except FileNotFoundError as e:
    print(e)  # or custom error msg
except Exception as e:
    print('WTF')
else:  # Only runs if we don't have an error, in other words, the expect doesn't throw an error
    print(f.read())
    f.close()
finally:  # It's gets executed anyway regardless of any error or not
    print('Executing Finally')
