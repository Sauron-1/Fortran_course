program main
    Integer*4 :: i=1, s=0
    Integer*4, parameter :: end=101
100 continue !loop
    s = s + i
    i = i + 1
    if (i < end) goto 100 !loop
    write(*, *) s
end program
