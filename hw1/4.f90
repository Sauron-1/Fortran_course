Program main
    Real*8 :: a, b, c
    write(*, *) 'Please input a, b, c'
    read(*, *) a, b, c
    if (a == 0) then
        write(*, *) 'a can''t be 0'
        stop
    endif
    write(*, *) 'Solutions are:'
    write(*, *) (-b + ((4, 0)*a*c-b**2)**0.5)/2/a
    write(*, *) (-b - ((4, 0)*a*c-b**2)**0.5)/2/a
End Program
