module Global
    implicit none
    !Scale and output info
    Integer, parameter :: nx = 101, ntend = 4
    !Grid
    Real, parameter :: x_range(2) = (/-2., 14./), &
        dx = (x_range(2) - x_range(1))/(nx-1)
    !Times to output
    Real, parameter :: tend(ntend) = (/1., 2., 3., 4./)
    
    !Global variables
    Real*4, save :: t, u(nx), x(nx), dt, s=1., CFL=0.1
    !$omp threadprivate(t, u, x, dt, s, CFL)
end module Global
