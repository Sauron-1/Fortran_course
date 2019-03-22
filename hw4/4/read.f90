program main
    !Copied from slides
    Character*20 string
    Integer :: number
    Real :: value
    open(8, file="FILE8-4.TXT")
    read(8, 100) number, value
    read(8, 300) string
    write(*, *) number, value, string
100 format(i6, f8.3)
300 format(a10)
    close(8)
end
