program main
    !Just a test program, print results calling functing "area".
    use area_module
    write(*, *) "Value of 'area(5.)': ", area(5.)
    write(*, *) "Value of 'area(3., 4.)': ", area(3., 4.)
end program
