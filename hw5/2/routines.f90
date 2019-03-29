module Routines
    use Global
    implicit none
    contains

        subroutine init
            implicit none
            Integer i
            forall (i = 1:nx)
                x(i) = (i - 1) * dx + x_range(1)
            end forall
            u = 1.5 + s * tanh(x)
            t = 0
        end subroutine init

        subroutine next_LW
            implicit none
            Real, save :: u_t(0:nx+1), a_t(1:nx+1)
            !$omp threadprivate(u_t, a_t)
            u_t(1:nx) = u
            u_t(0) = 1.5 + s * tanh(x_range(1))
            u_t(nx+1) = 1.5 + s * tanh(x_range(2))

            a_t = 1/2. * (u_t(0:nx) + u_t(1:nx+1))

            dt = CFL * dx / maxval(abs(a_t))

            u = u - dt/(4*dx) * (u_t(2:nx+1)**2 - u_t(0:nx-1)**2) + &
                1/4.*(dt/dx)**2 * (a_t(2:nx+1)*(u_t(2:nx+1)**2-u_t(1:nx)**2) - &
                                  a_t(1:nx)*(u_t(1:nx)**2-u_t(0:nx-1)**2))
            t = t + dt
        end subroutine next_LW

end module Routines
