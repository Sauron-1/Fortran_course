subroutine Str2num(str, num)
    implicit none
    Character (len=*) :: str
    Real num
    Integer :: inte=0, dicimal=1, i
    Logical :: dic_encountered = .false.

    !Tranverse the string, get the number as float dicimal number.
    do i = 1, len(str)
        if ('0' < str(i:i) .and. '9' > str(i:i)) then
            inte = inte*10 + iachar(str(i:i)) - iachar('0')
            if (dic_encountered) then
                dicimal = dicimal * 10
            end if
        else if (str(i:i) == '.') then
            dic_encountered = .true.
        end if
    end do

    !Choose to return Real or Integer, 
    !but I don't know if fortran suppports templete.
    if (dic_encountered) then
        num = Real(inte) / dicimal
    else
        num = inte
    end if
end subroutine Str2num

program main
    implicit none
    !Integer :: num1;
    Real :: num1, num2;
    Character (len=*), parameter :: str1='23456', str2='75.8'

    call Str2num(str1, num1)
    call Str2num(str2, num2)

    write(*, *) num1
    write(*, *) num2
end program
