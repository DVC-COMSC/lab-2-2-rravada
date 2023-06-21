def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    ov_hours = workhours - reg_hours
    reg_rate = 18.25 * workhours
    ov_rate = 0
    if ov_hours > 0:
        ov_rate = 27.78 * ov_hours
    total_wage= reg_rate+ov_rate
   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: {reg_rate}")
    print(f"Overtime hours: {ov_hours} Overtime Charge: {ov_rate:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return reg_rate , ov_rate , total_wage


if __name__ == '__main__':
    main()
