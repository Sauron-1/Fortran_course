program main
    use Global
    use Routines
    implicit none
    Integer :: i, j

    !$omp parallel do private(j)
    do i = 0, 1
        select case(i)
            case(0)
                s = 1
                call init
                open(10, file='parallel_0.dat', status='replace', form='unformatted')
                write(10) t, u
            case(1)
                s = -1
                call init
                open(11, file='parallel_1.dat', status='replace', form='unformatted')
                write(11) t, u
        end select

        do j = 1, ntend
            do while(t < tend(j))
                call next_LW
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
