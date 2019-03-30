program main
    !Two threads case.
    !Data will be saved to parallel_0.dat and parallel_1.dat
    use Global
    use Routines
    implicit none
    Integer :: i, j
    Real, parameter :: pi=3.14159265358979
    Character :: filename

    !$omp parallel do private(j)
    do i = 0, 1
        call init_without_u
        select case(i)
            case(0)
                u = exp(-(x/0.1)**2)
            case(1)
                u = exp(-((x-1)/0.1)**2) + exp(-((x+1)/0.1)**2)
        end select
        call init_u
        write(filename, '(i1)') i
        open(10+i, file='parallel'//filename//'.dat', &
            form='unformatted', status='replace')
        write(10+i) t, u

        do j = 1, ntend
            do while(t < tend(j))
                call next
            end do
            write(10+i) t, u
        end do

    end do
    !$omp end parallel do
end program
