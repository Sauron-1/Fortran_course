program main

    implicit none
    Integer, parameter :: x_size = 50 - (-50) +1, y_size = 100 - (-100) + 1
    Integer, parameter :: x_start = -50, x_step = 1, y_start = -100, y_step = 1
    Integer :: x(x_size), y(y_size), z(y_size, x_size)
    Integer :: i, j

    !Initialize x and y data.
    do i = 1, x_size
        x(i) = (i-1)*x_step + x_start
    end do
    do i = 1, y_size
        y(i) = (i-1)*y_step + y_start
    end do

    !Calculate z's value and print
    z = spread(x, 1, y_size)**2 + spread(y, 2, x_size)**2

    do i = 1, y_size
        do j = 1, x_size
            write(*, "(i7)", advance='no') z(i, j)
        end do
        write(*,*) ""
    end do

end program
