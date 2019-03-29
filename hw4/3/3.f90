program main
    implicit none
    Integer, parameter :: max_size = 8096 !Max numbers that the file can include
    Integer :: num, num_read, buf(max_size), num_count = 0
    Logical :: written = .false.

    write(0, *) "Input the number to insert:"
    read(*, *) num

    !Read file to buffer, and insert the input number
    open(10, file="numbers.txt", form="formatted")
    do
        read(10, *, end=100) num_read
        num_count = num_count + 1
        if (num_read > num .and. .not. written) then
            buf(num_count) = num
            num_count = num_count + 1
            written = .true.
        end if
        buf(num_count) = num_read
    end do
100 continue
    if (.not. written) then
        num_count = num_count + 1
        buf(num_count) = num
    end if
    
    !Write buffer to file
    rewind(10)
    do num = 1, num_count
        write(10, "(i5)") buf(num)
    end do
    close(10)
end program
