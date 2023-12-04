company = "'metatrade'"
software = "antivir"

t1 = "\nвітаємо Вас в нашій компанії: "
t2 = "\nКомпанія {0} звітує про виконання річного плана з розробки {1}\n"

print(t1 + company)
print(t2.format(company, software))