# Pwnable bof - 5 pt
`nc pwnable.kr 9000`
## Explanation
The `gets()` function does not check how many characters are being fed into the `char overflowme[32]`

This means we can overflow the buffer if you enter enough input. A string like the alphabet can be used to allow us to detect the change in the key better.

Using gdb, we can check whether the variable key has been changed to the alpahbet you specified

Once we find the amount of padding required (In this case, it is 52 letters long), we can overwrite the variable

Remember to use Little-endian format

Because we get segmentation fault before we can input anything into the shell, we can use cat to solve that problem.

## Code
`
(python -c "print 'A'*52 + '\xbe\xba\xfe\xca'";cat) | nc pwnable.kr 9000
`
## Flag
`daddy, I just pwned a buFFer :)`
