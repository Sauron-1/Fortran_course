program main
    !Parallel test. Use s = 1 and s = -1.
    !Output to parallel0.dat to parallel3.dat
    use Global
    use Routines
    implicit none
    Integer :: i, j
    Character :: filename

    !$omp parallel do private(j, filename)
    do i = 0, 3
        write(filename, '(i1)') i
        select case(i)
            case(0)
                s = 1
            case(1)
                s = -1
            case(2)
                s = 1
                CFL = 0.5
            case(3)
                s = 1
                CFL = 1
        end select
        call init
        open(10+i, file='parallel'//filename//'.dat', &
            status='replace', form='unformatted')
        write(10+i) t, u

        do j = 1, ntend
            do while(t < tend(j))
                call next_LW
            end do
            write(10+i) t, u
        end do

        close(10+i)
    end do
    !$omp end parallel do

end program
