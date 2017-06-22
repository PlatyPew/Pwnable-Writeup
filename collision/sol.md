# Pwnable collision - 3 pt
`ssh col@pwnable.kr -p2222` (pw:guest)

## Explanation:
The executable takes 20 characters as input. In the `check_password` function, it converts the characters you entered into hex values in groups of 5. For example, `AAAAAAAAAA` becomes `0x414141414141+0x414141414141=0x828282828282`

The function then retturns the value and checks if it's `0x21DD09EC`.

So if we can print out characters that add up to `0x21DD09EC`, we can solve this challenge

Remember to enter the values in Little-endian.

## Code:
``
./col `python -c "print '\x11\x11\x11\x01'*4+'\xa8\xc5\x98\x1d'"`
``

## Flag:
`daddy! I just managed to create a hash collision :)`
