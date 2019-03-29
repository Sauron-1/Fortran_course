module Global
    implicit none
    Integer, parameter :: nx = 101, ntend = 4, s = 1
    Real, parameter :: x_range(2) = (/-2., 14./), dx = (x_range(2) - x_range(1))/(nx-1)
    Real, parameter :: CFL = 0.1
    Real, parameter :: tend(ntend) = (/1., 2., 3., 4./)
    
    Real*4, save :: t, u(nx), x(nx), a(nx), dt
end module Global
