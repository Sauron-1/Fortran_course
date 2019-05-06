module parameters
    !Parameters given in the problem.
    implicit none
    Real*8, parameter :: pi = 3.14159265358979
    Real*8, parameter :: Re = 6376e3, B0 = 3.12e-5, mu = pi*4e-7
    Real*8, parameter :: rho = 1.6726219e-21, L = 6.6
    Integer, parameter :: nf = 6
    Real*8, parameter :: fs(nf) = (/0.019, 0.051, 0.082, 0.113, 0.144, 0.175/)
end module parameters
