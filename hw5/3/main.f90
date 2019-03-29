program main
    use Global
    use Routines
    implicit none
    Integer i

    open(10, file='data.dat', form='unformatted', status='replace')

    call init

    write(10) t, u

    do i = 1, ntend
        do while(t < tend(i))
            call next
        end do
        write(10) t, u
    end do

    close(10)
end program
