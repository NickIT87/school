company = "'metatrade'"
software = "antivir"

t1 = "\n вітаємо вас в нашій компанії: "
t2 = "\n Компанія {0} звітує про виконання річного плана з розробки {1}\n"

print(t1 + company)
print(t2.format(company, software))