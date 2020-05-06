credit = eval ( input("Укажите сумму кредита:") )
credit_rate = eval ( input("Укажите процентную ставку:") )
credit_years = eval ( input("Укажите срок кредита:") )
final_sum = credit + credit / 100 * credit_rate * credit_years
month_pay = final_sum // credit_years
print ("сумма к выплате за", credit_years , "лет составит:", final_sum)
print("платеж в месяц составит: ", month_pay)