# Pwnable fd - 1 pt
`ssh fd@pwnable.kr -p2222` (pw:guest)

## Explanation:
The executable checks for an argument an uses the `atoi()` function to convert the argument into an integer.

Obviously, we need to enter in an actual number or it will output a 0. (atoi functions returns 0 if not given a number)

Using the `read()` function, by making the file descriptor 0, it takes a stdin (Standard input).

The `strcmp()` function compares the strings and outputs a 0 if the strings are the same. In this case, the code is `if(!strcmp("LETMEWIN\n", buf))`. The `\n` acts as a break line.

Entering `LETMEWIN` and pressing enter will give you the flag.

## Answer:
`echo LETMEWIN | ./fd 4660`

## Flag:
`mommy! I think I know what a file descriptor is!!`
