function lagrange(x)
    implicit none
    Real :: lagrange, x, ret
    Integer :: length, i
    Real, parameter :: xs(*) = (/1.05, 1.1, 1.15, 1.2/)
    Real, parameter :: ys(*) = (/2.12, 2.2, 2.17, 2.32/)

    ret = 0.
    length = size(xs)
    do i = 1, length
        ret = ret + &
                   ys(i)*product(x-xs(1:i-1))*product(x-xs(i+1:length))/ &
                   product(xs(i)-xs(1:i-1))/product(xs(i)-xs(i+1:length))
    end do
    lagrange = ret
end function lagrange

program main
    implicit none
    Real :: lagrange
    write(*, *) 'f(1.075) = ', lagrange(1.075)
    write(*, *) 'f(1.175) = ', lagrange(1.175)
end program
