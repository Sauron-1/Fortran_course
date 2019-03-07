program main

    implicit none
    Integer :: student_number, number_max, student(5), i, j
    Integer, allocatable :: scores(:, :), passed(:, :)
    Real :: average
    Real, allocatable :: averages(:)

    !Read max number of students
    write(0, *) "Please input max number of students: "
    read(*, *) number_max
    
    allocate(scores(number_max, 6))
    allocate(averages(number_max))
    student_number = 0

    !Read scores, until student serial number -1 encountered
    do i = 1, number_max
        write(0, *) "Input a student's score"
        write(0, *) "Serial number -1 will stop inputing"
        write(0, *) "Format: Serial Course1 Course2 Course3 Course4"
        read(*, *) student
        if (student(1) /= -1) then
            student_number = student_number + 1
            scores(student_number, :5) = student
        else
            exit
        end if
    end do

    !Calculations and outputs
    averages = sum(scores(:student_number, 2:), 2) / 4.
    average = sum(averages) / student_number
    write(*, *) "Averge score is ", average
    do i = 1, student_number
        if (averages(i) > average) then
            do j = 1, 5
                write(*, "(i7)", advance="no") scores(i, j)
            end do
            write(*, *) ""
        end if
    end do

end program
