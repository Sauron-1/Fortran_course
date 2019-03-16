subroutine encrypt(str)
    Character (len=*) :: str
    Integer :: i

    !Just do what is asked.
    do i = 0, len(str)
        if (str(i:i) >= 'A' .and. str(i:i) <= 'Z') then
            str(i:i) = achar(iachar('Z') - iachar(str(i:i)) + iachar('A'))
        else if (str(i:i) >= 'a' .and. str(i:i) <= 'z') then
            str(i:i) = achar(iachar('z') - iachar(str(i:i)) + iachar('a'))
        end if
    end do
end subroutine encrypt

program main
    Character (len=:), allocatable :: str
    Integer :: l

    write(0, *) "Input max string length"
    read(*, *) l

    allocate(Character (len=l) :: str)

    write(0, *) "Input the string"
    read(*, *) str

    !Remove the extra length of the string.
    str = trim(str)
    call encrypt(str)

    write(*, *) str
end program
