program main
    implicit none
    Real :: a, b, h, s=0.
    Integer :: n, i
    Real, allocatable :: x(:)

    write(0, *) 'Input a, b, n'
    read(*, *) a, b, n
    h = (b - a)/n

    allocate(x(n+1))
    forall (i = 1:n+1)
        x(i) = a + (i-1)*h
    end forall

    x = sin(x)
    !Calculate with array operation.
    s = sum(h*(x(:n)+x(2:))/2.)

    write(*, 100) a, b, n
    write(*, 200) s

100 format(1x, 'a = ', f10.3, 3x, 'b = ', f10.3, 3x, 'n=', i4)
200 format(1x, 's = ', f15.8)
end program
