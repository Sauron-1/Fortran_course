module Global
    implicit none
    Integer, parameter :: nx = 101, ntend = 4
    Real, parameter :: x_range(2) = (/-2, 2/), tend(ntend) = (/1., 2., 3., 4./)
    Real, parameter :: b = 0.01, dx = (x_range(2) - x_range(1))/(nx-1)
    !u_last storing u's value in last step for calculating u_next
    Real, save :: x(nx), t, dt, u(nx), u_last(nx), u_next(nx), CFL=0.1
    !$omp threadprivate(x, t, dt, u, u_last, u_next, CFL)
end module Global
