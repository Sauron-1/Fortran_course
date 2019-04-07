module runge_kutta
    implicit none
    contains
        subroutine RK4_step(f, y0, n, x, dx, yout)
            !Run one step of 4-order RK.
            Real :: y0(n), yout(n), x, dx
            Real, allocatable :: k1(:), k2(:), k3(:), k4(:)
            Integer :: n, i, j
            Real, external :: f

            allocate(k1(n))
            allocate(k2(n))
            allocate(k3(n))
            allocate(k4(n))
            
            k1 = f(x, y0)
            k2 = f(x + dx/2., y0 + k1*dx/2.)
            k3 = f(x + dx/2., y0 + k2*dx/2.)
            k4 = f(x + dx, y0 + dx*k3)

            yout = y0 + dx/6*(k1 + 2*k2 + 2*k3 + k4)

            deallocate(k1)
            deallocate(k2)
            deallocate(k3)
            deallocate(k4)
        end subroutine RK4_step

        subroutine RK4(f, y0, n, x, dx, steps, yout)
            !yout here is array of outputs in each step.
            Real :: y0(n), yout(steps, n), x, dx
            Integer :: n, steps, i
            Real, external :: f

            call RK4_step(f, y0, n, x, dx, yout(1, :))
            do i = 2, steps
                call RK4_step(f, yout(i-1, :), n, x+(i-1)*dx, dx, yout(i, :))
            end do
        end subroutine RK4
end module runge_kutta
