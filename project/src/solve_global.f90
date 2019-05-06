module s_global
    use parameters
    use functions
    implicit none
    !Boundary conditions. y2 is not used according to report.
    Real*8, parameter :: sm1 = asin(sqrt(1./L)), sm2 = pi - asin(sqrt(1./L))
    Real*8, parameter :: y1 = 0., y2 = 0.
    !Step number and step size.
    Integer*8, parameter :: ntheta = 201
    Real*8, parameter :: dtheta = (sm2-sm1)/(ntheta-1)
end module s_global
