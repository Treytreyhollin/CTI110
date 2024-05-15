totgross = 0
tot_ovt_pay = 0

tot_reg_hour_pay = 0

emp_num = 0 





# header

print('-------------------------------------------------------------------------------------------')

print(f"{'Employee Name':<20s}{'Pay Rate':>10s}")

print(f"{'Number of Hours Worked':<20s}{'Overtime':>15s}")

print(f"{'Overtime Pay':<20s}{'Reghour Pay':>15s}")

print(f"{'Gross Pay':<20s}{'':>15s}")

print('-------------------------------------------------------------------------------------------')



# get info

 
    # employee's name

emp_name = input("Enter the name of the employee or 'Done' to terminate: ")

    # to terminate
if emp_name == "done":
       break



    # Increments 
       emp_num+= 1

       hours_worked = float(input(f"How many hours did {emp_name} work?: "))
       pay_rate = float(input(f"What is {emp_name}'s pay rate?"))

    # overtime

if hours_worked > 40:

        # Calculate ot hours
        ovt = hours_worked - 40

        # ! amount to the employee for overtime hours !

        ovt_pay = ovt * (pay_rate * 1.5)
        reg_hour_pay = 40 * pay_rate

else:

        ovt = 0
        reg_hour_pay = hours_worked * pay_rate
        ovt_pay = 0

    #gross pay

        gross_pay = reg_hour_pay + ovt_pay


        tot_ovt_pay += ovt_pay

        tot_reg_hour_pay += reg_hour_pay

        totgross += gross_pay



    # ! informa !

        print('\n'f"employee name: {emp_name:<20s}")

        print('\n' + f"{'Hours worked':<17s}{'Pay ate':>12s}{'OT':>17s} {'OT pay':>17s}{'Regular hour pay':>17s}{'GrossPay':>17s}")

        print('-------------------------------_----------------------------------------------')

        print(f"{hours_worked:2,.2f} ${pay_rate:22,.2f} {ovt:15,.2f} ${tot_ovt_pay:17,.2f} ${reg_hour_pay:17,.2f}")
        print()

        print(f"Total number of employees: {emp_num}")
        print(f"Total amount paid for overtime: {tot_ovt_pay}")
        print(f"Total amount paid for regular hours: {reg_hour_pay}")
        print(f"Total amount paid in gross: {totgross}")
