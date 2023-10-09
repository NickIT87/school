import pandas as pd

def generate_excel(filename):
    df = pd.DataFrame(
        {
            'Имя': ['Алиса', 'Боб', 'Чарли'],
            'Возраст': [25, 30, 35]
        }
    )
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer._save()

generate_excel("example.xlsx")
