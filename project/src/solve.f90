Program main
    use runge_kutta
    use equation
    use s_global
    use functions
    implicit none
    Integer*8 :: n=2, i, num
    Real*8 :: ys1(ntheta, 2), ys(ntheta), t, thetas(ntheta), ss(ntheta)

    !Calculate s and theta for plotting.
    forall (i=1:ntheta)
        thetas(i) = sm1 + i*dtheta
    end forall
    do i = 1, ntheta
        ss(i) = s(thetas(i))
    end do

    open(10, file='test.dat', form='unformatted')
    write(10) thetas
    write(10) ss
    
    !Calculate for all fs and save the result.
    do num = 1, nf
        f = fs(num)
        call RK4(diffs, (/y1, 1d-7/), n, sm1, dtheta, ntheta, ys1)
        do i = 1, ntheta
            ys(i) = ys1(i, 1)*h(thetas(i))
        end do
        write(10) ys
    end do
    close(10)
end program
