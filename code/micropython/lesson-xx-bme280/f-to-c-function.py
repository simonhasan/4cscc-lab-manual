tempC = 31
tempF = 47

def convert_f_to_c(temp_f):
    temp_c = 5 / 9 * (temp_f - 32)
    return temp_c

def convert_c_to_f(temp_c):
    temp_f = (9 / 5) * temp_c + 32
    return temp_f

print(convert_f_to_c(tempF))
print(convert_c_to_f(tempC))