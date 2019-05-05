def gross(b):
    grossSalary=b+(0.3*b)+(0.8*b)
    return grossSalary

def net(g,l):
    pf=1800
    leaveDeduction=0
    if(l>1):
        leaveDeduction=(l-1)*500;
    netSalary=g-pf-leaveDeduction
    return netSalary

basicPay = input("Basic pay of employee:")
leaveDays= input("No.of leaves taken:")

grossSalary=gross(int(basicPay))
netSalary=net(grossSalary,int(leaveDays))

print("Gross Salary of employee is: "+str(grossSalary))
print("Net Salary of emplyee is: "+str(netSalary))
