program main
    !Copied from slides
    Integer :: number = 123
    Real :: value = 987.65
    Character(len = *), parameter :: string = "AN EXAMPLE"
    open(8, file="FILE8-4.TXT")
    write(8, 100) number
    write(8, 200) value
    write(8, 300) string
100 format(i6)
200 format(f8.3)
300 format(a10)
    close(8)
end
