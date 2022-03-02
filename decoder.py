
def oct_to_dec(code):
    decimal_value = 0
    base = 1

    while (code):
        last_digit = int(code) % 10
        code = int(int(code) / 10)
        decimal_value += last_digit * base
        base = base * 8
    return str(decimal_value)



def decode(code):
  split_code = code.split()
  result = ""
  for n in split_code:
    result = result + oct_to_dec(int(n)) + " "
  print(result.strip())
  return result.strip()
  # return result


