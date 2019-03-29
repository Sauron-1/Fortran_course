program main
    implicit none
    Integer :: a, b, c
    
    !Try every possibilities.
    do a = 1, 50
        do b = a, 50
            do c = b, 50
                if (a**2 + b**2 == c**2) then
                    write(*, 100) a, b, c
                end if
            end do
        end do
    end do

100 format(i2, "^2 + ", i2, "^2= ", i2, "^2")

end program
