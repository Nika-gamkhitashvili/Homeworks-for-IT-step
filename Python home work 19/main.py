def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    s = s.upper()
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            num += roman_dict[s[i + 1]] - roman_dict[s[i]]
            i += 2
        else:
            num += roman_dict[s[i]]
            i += 1
    return num


# შეტანის ფუნქცია
def main():
    while True:
        roman_input = input("შეიტანეთ რომაული რიცხვი (ან 'გასვლა' გასასვლელად): ")
        if roman_input.lower() == 'გასვლა':
            break
        try:
            result = roman_to_int(roman_input)
            print(f"რომაული რიცხვი {roman_input} არის {result}")
        except KeyError:
            print("შეიტანეთ სწორი რომაული რიცხვი.")


if __name__ == "__main__":
    main()
