#pizza_calculator получаем число с помощью функции eval ()
number_of_pizza = eval(input("Сколько пицц вы хоите?")) #запрашиваем количество пицц
cost_per_pizza = eval (input("Сколько стоит пицца")) #запрашиваем стоимость пиццы по меню
subtotal = number_of_pizza * cost_per_pizza #посчитываем подытог
#посчитываем сумму налога с продаж по ставке 8%
tax_rate = 0.08
sales_tax = subtotal * tax_rate

#приплюсовываем налог с продаж к подытогу и получаем итог
total = subtotal + sales_tax

#показываем покупателю общую сумму к оплате в том числе налог

print ("Полная стоимость $", total)
print("За пиццу $", subtotal)
print("Налог с продаж $", sales_tax)