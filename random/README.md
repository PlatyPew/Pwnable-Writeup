# Pwnable random - 1 pt
`ssh random@pwnable.kr -p2222` (pw:guest)

## Explanation
The `rand()` function doesn't actually produce a random number. Instead, it generates a pseudo-random number by transforming variables here and there. For example, if the variables are all the same, then it will constantly produce the same number. That's why no matter how many times the code is recompiled, the number generated remanins the same.

In this case, `rand()` generates the value `1804289383`.

The `if` statement checks whether the value you put in `xor` the number generated is equals to `0xdeadbeef`

By taking `0xdeadbeef ^ 1804289383`, you can find the number needed to input in.

## Code
`echo 3039230856 | ./random`

## Flag
`Mommy, I thought libc random is unpredictable...`
