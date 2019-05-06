module equation
    !Most of functions here are calculated by sympy
    use parameters
    use functions
    implicit none
    Real*8 :: f
    contains
        
        !Second derivative of s to theta
        function ps_ptheta_2(theta)
            Real*8 :: ps_ptheta_2, theta
            
            ps_ptheta_2 = -L*Re*(36*sqrt(-3*sin(theta)**2 + 4)*sin(theta)**4 - &
                66*sqrt(-3*sin(theta)**2 + 4)*sin(theta)**2 + 28*sqrt(-3*sin(theta)**2 + 4) + &
                36*sqrt(3.)*cos(theta)**5 - 4*sqrt(3.)*cos(theta))*cos(theta)/&
                (6*sqrt(3.)*sqrt(3*cos(theta)**2 + 1)*cos(theta)**3 + &
                2*sqrt(3.)*sqrt(3*cos(theta)**2 + 1)*cos(theta) + 18*cos(theta)**4 + &
                9*cos(theta)**2 + 1)
        end function ps_ptheta_2

        !Derivative of s to theta
        function ps_ptheta(theta)
            Real*8 :: ps_ptheta, theta

            ps_ptheta = -L*Re*(3*sqrt(3*cos(theta)**2 + 1)*cos(theta)**2 + &
                sqrt(3*cos(theta)**2 + 1) + 3*sqrt(3.)*cos(theta)**3 + &
                sqrt(3.)*cos(theta))*sin(theta)/(sqrt(3.)*&
                sqrt(3*cos(theta)**2 + 1)*cos(theta) + 3*cos(theta)**2 + 1)
        end function ps_ptheta

        !Index of original equation. See report for detail
        function o_B(theta)
            Real*8 :: o_B, theta

            o_B = 3*(sqrt(3.)*sqrt(3*cos(theta)**2 + 1)*cos(theta) + &
                3*cos(theta)**2 + 1)*cos(theta)/(L*Re*(3*cos(theta)**2 + 1)*&
                (3*sqrt(3*cos(theta)**2 + 1)*cos(theta)**2 + &
                sqrt(3*cos(theta)**2 + 1) + 3*sqrt(3.)*cos(theta)**3 + sqrt(3.)*cos(theta)))
        end function o_B

        !Index of original equation. See report for detail
        function o_C(theta)
            Real*8 :: o_C, theta
            o_C = (2*pi*f*sqrt(mu*rho)/B(theta))**2
        end function o_C

        !Index of trnasformed equarion. See report for detail
        function t_B(theta)
            Real*8 :: t_B, theta
            t_B = -ps_ptheta_2(theta)/ps_ptheta(theta) + &
            o_B(theta)*ps_ptheta(theta)
        end function t_B

        !Index of trnasformed equarion. See report for detail
        function t_C(theta)
            Real*8 :: t_C, theta
            t_C = o_C(theta)*(ps_ptheta(theta)**2)
        end function t_C

        !The equation. See report for detail
        subroutine diffs(theta, ys, ret)
            Real*8 :: ys(2), theta
            Real*8 :: ret(2)

            ret(1) = ys(2)
            ret(2) = -t_B(theta)*ys(2) - t_C(theta)*ys(1)
        end subroutine diffs

end module equation
