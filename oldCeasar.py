def ceasar(plain, key=3):
    cipher = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = {}
    start = ord('a') - key

    for i in range(0, len(alphabets) - key):
        ch = alphabets[i]
        encrypt[ch] = chr(ord(ch) + key)

    for i in range(len(alphabets) - key, len(alphabets)):
        ch = alphabets[i]
        encrypt[ch] = chr(start + key)
        start += 1

    for ch in plain:
        if not str.isalpha(ch):
            cipher += ch
        elif str(ch).isupper():
            cipher += str.upper(encrypt[str.lower(ch)])
        else:
            cipher += encrypt[ch]

    return cipher


def main():
    print('\nEnter some text : ', end='')
    plain = input()
    cipher = ceasar(plain)
    print('The cipher text is : ' + cipher)


if __name__ == '__main__':
    main()
