function f(t, y)
    !dy/dt = f(t, y)
    Real :: f
    f = y**2 * cos(t)
end function f

program main
    use runge_kutta
    implicit none
    Real :: y0(1) = (/1/), xr(2) = (/0., 0.8/)
    Real, allocatable :: x(:), yout(:, :)
    Integer :: n = 100, i  !steps to run
    Real, external :: f

    allocate(x(n))
    allocate(yout(n, 1))
    forall (i = 1:n)
        x(i) = xr(1) + (xr(2) - xr(1))/(n-1)*i
    end forall

    call RK4(f, y0, 1, xr(1), (xr(2)-xr(1))/(n-1), n, yout)

    open(10, file='res.dat', form='unformatted')
    write(10) x 
    write(10) yout
    close(10)
end program
