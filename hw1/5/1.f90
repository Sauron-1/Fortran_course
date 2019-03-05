program main
    Real(4) :: income, tax
    write(*, *) "Please input your monthly income"
    read(*, *) income
    if (income < 1000) then
        tax = income*0.03
    else if (income < 5000) then
        tax = income*0.03 + (income-1000)*0.07
    else
        tax = income*0.03 + (income-1000)*0.07 + (income-5000)*0.05
    end if
    write(*, *) "tax: ", tax
end program
