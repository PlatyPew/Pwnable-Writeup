# Pwnable flag - 7 pt
Download binary from http://pwnable.kr/play.php

## Explanation
By using `strings flag`, we can determine that it has been compressed by UPX.

Upon decompressing it, open up `flag` with `gdb` and `disas main`.

We can see that `<flag> @ 0x6c2070`. Print the value in that address using `printf` and `*` to dereference the address.

## Code
1. `upx -d flag`
2. `gdb flag`
3. `printf "%s",*0x6c2070`

## Flag
`UPX...? sounds like a delivery service :)`
.
