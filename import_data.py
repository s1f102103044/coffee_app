import csv
from authtest.models import Coffee

# CSVファイルのパス（Raw Stringを使用）
csv_file_path = r'C:\Users\iniad\Documents\CS_exercise\team-project-2022-be4\COFFEE.csv'

with open(csv_file_path, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        coffee = Coffee(
            co_name=row["co_name"], 
            roast_level=row["roast_level"], 
            acidity=row["acidity"], 
            com=row["com"],
            three_letters=row["three_letters"]
        )
        coffee.save()

'''
以下のコマンドを「python manage.py shell」で開いたシェルで打ってCSVファイルをインポートした
exec(open(r'C:\Users\iniad\Documents\CS_exercise\team-project-2022-be4\import_data.py', encoding='utf-8').read())
'''