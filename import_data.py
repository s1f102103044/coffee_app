import csv
from django.db import transaction
from authtest.models import Coffee

# CSVファイルのパス（Raw Stringを使用）
csv_file_path = r'C:\Users\iniad\Documents\CS_exercise\team-project-2022-be4\COFFEE.csv'

# データベースの変更をトランザクションブロック内で実行
with transaction.atomic():
    # 既存のデータをクリアする場合は、以下の行のコメントを解除
    Coffee.objects.all().delete()

    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # get_or_createを使用して、既存のオブジェクトを取得または新しく作成
            coffee, created = Coffee.objects.get_or_create(
                co_name=row["co_name"],
                defaults={
                    'roast_level': row["roast_level"],
                    'acidity': row["acidity"],
                    'com': row["com"],
                    'three_letters': row["three_letters"]
                }
            )
            # オブジェクトが既に存在する場合（createdがFalseの場合）、データを更新
            if not created:
                coffee.roast_level = row["roast_level"]
                coffee.acidity = row["acidity"]
                coffee.com = row["com"]
                coffee.three_letters = row["three_letters"]
                coffee.save()

'''
以下のコマンドを「python manage.py shell」で開いたシェルで打ってCSVファイルをインポートした
exec(open(r'C:\Users\iniad\Documents\CS_exercise\team-project-2022-be4\import_data.py', encoding='utf-8').read())
'''