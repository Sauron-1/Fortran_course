module runge_kutta
    !4-order Runge-Kutta
    implicit none
    contains
        subroutine RK4_step(f, y0, n, x, dx, yout)
            !Run one step of 4-order RK.
            Real*8 :: y0(n), yout(n), x, dx
            Real*8 :: k1(n), k2(n), k3(n), k4(n)
            Integer*8 :: n, i, j
            external :: f

            call f(x, y0, k1)
            call f(x + dx/2., y0 + k1*dx/2., k2)
            call f(x + dx/2., y0 + k2*dx/2., k3)
            call f(x + dx, y0 + dx*k3, k4)

            yout = y0 + dx/6.*(k1 + 2*k2 + 2*k3 + k4)
        end subroutine RK4_step

        subroutine RK4(f, y0, n, x, dx, steps, yout)
            !yout here is array of outputs in each step.
            Real*8 :: y0(n), yout(steps, n), x, dx
            Integer*8 :: n, steps, i
            external :: f

            call RK4_step(f, y0, n, x, dx, yout(1, :))
            do i = 2, steps
                call RK4_step(f, yout(i-1, :), n, x+(i-1)*dx, dx, yout(i, :))
            end do
        end subroutine RK4
end module runge_kutta
