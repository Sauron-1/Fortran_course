subroutine max(A, B, m, n, k)
    implicit none
    Real :: A(:, :), B(:)
    Integer :: m, n, k
    
    B = maxval(A, k)
end subroutine max

program main
    Real, allocatable :: A(:, :), B(:)
    Integer :: m, n, k

    interface
        subroutine max(A, B, m, n, k)
            Real :: A(:, :), B(:)
            Integer :: m, n, k
        end subroutine max
    end interface

    write(0, *) "Input m, n, k"
    read(*, *) m, n, k
    allocate(A(m, n))
    if (k == 1) then
        allocate(B(n))
    else
        allocate(B(m))
    end if

    write(0, *) "Input A"
    read(*, *) A

    call max(A, B, m, n, k)

    write(*, *) B
end program
