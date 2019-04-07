program main
    use util
    !There are still bugs in this program.
    !Some times QR-algorithm is not convergent, and this program gives wrong answer.
    !i.e. p = (/-1, 1, -1, 1/), x = 1 is a root, but can't be given here.
    Real*8, allocatable :: p(:)
    Real*8, allocatable :: x(:)
    Integer :: n, i

    write(0, *) 'Input order of the polynomial'
    read(*, *) n
    allocate(p(n+1))
    allocate(x(n))

    write(0, *) 'Input coefficients p(i)'
    write(0, *) 'format: p(1) + p(2) * x + ... + p(n+1) * x^n'
    read(*, *) p

    call solve(p, x, n)
    write(*, *) 'real roots are:'
    do i = 1, n
        write(*, *) x(i)
    end do

end program main
