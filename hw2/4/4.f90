function S(m, n, k)
    !Generate array from m-k to n-k
    Integer :: numbers(m-k:n-k), i
    forall (i=m-k:n-k) numbers(i) = i

    S = sum(numbers**2)
end function S

program main
    write(*, *) S(1, 100, 0)
    write(*, *) S(10, 100, 5)
end program
