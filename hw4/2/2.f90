program main
    implicit none
    Integer, parameter :: number_conunt=100
    Integer*4 :: i, n

    !Generate and write numbers
    open(20, file="origin.dat", form="unformatted")
    call srand(100)
    do i = 1, number_conunt
        write(20) irand()
    end do
    close(20)

    !Write all numbers read but the odds
    open(30, file="origin.dat", form="unformatted")
    open(40, file="no_odd.dat", form="unformatted")
    do
        read(30, end=100) n
        if (mod(n, 2) == 0) then
            write(40) n
        end if
    end do
    100 continue
end program
