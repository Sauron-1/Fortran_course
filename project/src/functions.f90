module functions
    !Functions given in the problem.
    use parameters
    implicit none
    contains

        function s(theta)
            Real*8 :: theta, s
            s = L*Re/2 * (cos(theta)*sqrt(1+3*(cos(theta))**2) + &
                1/sqrt(3.)*log(sqrt(1+3*(cos(theta))**2)+sqrt(3.)*cos(theta)))
        end function s

        function r(theta)
            Real*8 :: r, theta
            r = L*Re*(sin(theta))**2
        end function r

        function B(theta)
            Real*8 :: B, theta
            B = B0/(L**3) * sqrt((1+3*(cos(theta))**2)) / (sin(theta))**6
        end function B

        function h(theta)
            Real*8 :: h, theta
            h = r(theta) * sin(theta)
        end function h

end module functions
