module util
    implicit none
    contains
        subroutine QR(a, q, r, n)
            !q and r will be QR decomposition of a.
            !a, q, and r should be n*n array

            Real*8 :: a(:, :), q(:, :), r(:, :)
            Integer :: n, i
            Real*8, allocatable :: e(:, :), u(:), v(:, :), h(:, :)
            Real*8 :: alpha

            allocate(e(n, n))
            allocate(u(n))
            allocate(v(n, 1))
            allocate(h(n, n))

            e = 0
            forall (i = 1:n)
                e(i, i) = 1
            end forall
            r(:, :) = a
            q(:, :) = e


            do i = 1, n-1
                u = 0
                v = 0
                h(:, :) = e
                alpha = sqrt(sum(r(i:, i)**2))
                u(i:) = r(i:, i) - e(i:, i)*alpha
                v(i:, 1) = u(i:) / sqrt(sum(u(i:)**2))
                h(i:, i:) = e(i:, i:) - 2*matmul(v(i:, :), transpose(v(i:, :)))
                r(:, :) = matmul(h, r)
                q(:, :) = matmul(q, transpose(h))
            end do
            r(:, :) = matmul(transpose(q), a)

            deallocate(e)
            deallocate(u)
            deallocate(v)
            deallocate(h)

        end subroutine QR

        subroutine eigen(a, x, n, e, max_step)
            !eigen(a, x, n[, e=1e-5, max_step=2000])
            !x will be a's eigenvalues.
            !a should be shaped n*n, x's size should be n

            Real*8 :: a(:, :), eo
            Real*8 :: x(:)
            Real*8, optional :: e
            Integer, optional :: max_step
            Integer :: n, i, max_stepo, j, num
            Real*8 :: error
            Real*8, allocatable :: q(:, :), r(:, :), a_t(:, :)
            Logical, allocatable :: mask(:, :)
            Logical :: flag

            eo = 1e-5
            max_stepo = 2000
            if (present(e)) eo = e
            if (present(max_step)) max_stepo = max_step

            allocate(q(n, n))
            allocate(r(n, n))
            allocate(a_t(n, n))
            allocate(mask(n, n))

            mask = .false.
            forall (i = 2:n)
                forall (j = 1:i-1)
                    mask(i, j) = .true.
                end forall
            end forall

            a_t(:, :) = a

            do i = 1, max_stepo
                error = maxval(abs(a_t), mask=mask)
                if (error < eo) then
                    goto 100
                end if
                call QR(a_t, q, r, n)
                a_t(:, :) = matmul(r, q)
            end do
        100 continue
            num = 0
            do i = 1, n
                flag = .true.
                do j = 1, i-1
                    if (a_t(i, j) > eo) flag = .false.
                end do
                do j = i+1, n
                    if (a_t(j, i) > eo) flag = .false.
                end do
                if (flag) then
                    num = num + 1
                    x(num) = a_t(i, i)
                end if
            end do
            n = num

            deallocate(q)
            deallocate(r)
            deallocate(a_t)
            deallocate(mask)

        end subroutine eigen

        subroutine solve(p, x, n)
            !p(1) + p(2) * x + ... + p(n+1) * x**n

            Real*8 :: p(:)
            Real*8 :: x(:)
            Integer :: n, i
            Real*8, allocatable :: m(:, :)

            allocate(m(n, n))

            m = 0
            forall (i = 1:n-1)
                m(i+1, i) = 1
            end forall
            m(:, n) = -p(:n)/p(n+1)

            call eigen(m, x, n)

            deallocate(m)

        end subroutine solve

end module util
