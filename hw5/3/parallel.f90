program main
    use Global
    use Routines
    implicit none
    Integer :: i, j
    Real, parameter :: pi=3.14159265358979

    !$omp parallel do private(j)
    do i = 0, 1
        call init_without_u
        select case(i)
            case(0)
                u = exp(-(x/0.1)**2)
                open(10, file='parallel_0.dat', form='unformatted', status='replace')
                write(10) t, u
            case(1)
                u = exp(-((x-1)/0.1)**2) + exp(-((x+1)/0.1)**2)
                open(11, file='parallel_1.dat', form='unformatted', status='replace')
                write(11) t, u
        end select
        call init_u

        do j = 1, ntend
            do while(t < tend(j))
                call next
            end do

            select case(i)
                case(0)
                    write(10) t, u
                case(1)
                    write(11) t, u
            end select

        end do

    end do
    !$omp end parallel do
end program
