program main

    implicit none
    Integer*4 :: prime(200), i, j

    !Generate prime number table.
    !If prime(i) == 1, then i is a prime number.
    do i = 1, 200
        prime(i) = 1
    end do
    prime(1) = 0
    do i = 2, 200
        do j = i, 200/i + 1
            if (i*j > 200) then
                exit
            end if
            prime(i*j) = 0
        end do
    end do

    !Only print the first match.
    do i = 100, 200
        if (mod(i, 2) == 0) then
            do j = 1, i
                if (prime(j)==1 .and. prime(i-j)==1) then
                    write(*, *) i, ' = ', j, ' + ', i-j
                    exit
                end if
            end do
        end if
    end do

end program
