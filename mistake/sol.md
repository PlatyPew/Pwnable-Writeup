# Pwnable mistake - 1 pt
`ssh mistake@pwnable.kr -p2222` (pw:guest)

## Explanation
Due to operator precedence, the statement `fd=open("/home/mistake/password",O-RDONLY,0400) < 0` does not give the desired output

Since `<` is before `=` in the order of operators, the `if` statement first checks if `open() < 0`. Since the file exists, `open()` returns 1.

Since `1 < 0` is not true, it returns 0. Therefore `fd = 0`. Now it does not read from the file but instead from stdin because of `read(0,pw_buf,PW_LEN)`

So all we have to do is input the after value of the `xor()` function and the before value

Example, `xor("AAAAAAAAAA",10)` returns `@@@@@@@@@@`

## Code
`
(echo @@@@@@@@@@; echo AAAAAAAAAA) | ./mistake
`

## Flag
`Mommy, the operator priority always confuses me :(`
