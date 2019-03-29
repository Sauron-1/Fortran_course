module Global
    implicit none
    Integer, parameter :: nx = 101, ntend = 4
    Real, parameter :: x_range(2) = (/-2, 2/), tend(ntend) = (/1., 2., 3., 4./)
    Real, parameter :: b = 0.01, dx = (x_range(2) - x_range(1))/(nx-1), CFL=0.2
    Real, save :: x(nx), t, dt, u(nx), u_last(nx), u_next(nx)
end module Global
