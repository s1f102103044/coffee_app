from django.shortcuts import render
from .models import Coffee
from django.http import JsonResponse
from django.conf import settings

def home(request):
    coffees = Coffee.objects.all()
    if request.method == 'POST':
        selected_flavors = request.POST.getlist('flavor')  # チェックボックスの値をリストで取得

        # チェックボックスの値（英語）からcom属性の値（日本語）へのマッピング
        flavor_mapping = {
            "candied_citrus":"キャンディードシトラス",
            "sweet_citrus":"スイートシトラス",
            "grapefruit":"グレープフルーツ",
            "lemon":"レモン",
            "orange":"オレンジ",
            "milk_chocolate":"ミルクチョコレート",
            "dark_chocolate":"ダークチョコレート",
            "chocolate":"チョコレート",
            "cocoa":"ココア",
            "cinnamon":"シナモン",
            "spice":"スパイス",
            "herb":"ハーブ",
            "apple":"リンゴ",
            "blueberry":"ブルーベリー",
            "berry":",ベリー類",
            "raisin":"レーズン",
            "nuts":"ナッツ",
            "roasted_nuts":"煎ったナッツ",
            "pecan_nuts":"ピーカンナッツ",
            "roasted_veg":"ローストした野菜",
            "caramel":"カラメル",
            "cheese":"チーズ",
            "toffee":"トフィー",
            "better":"バター",
            "maple":"メープル",
            "oatmeal":"オートミール",
            "caramel2":"キャラメル",
            "currant":"カラント(スグリ)"
        }

        # 選択されたフレーバーを日本語に変換
        selected_flavors_jp = [flavor_mapping.get(flavor, "") for flavor in selected_flavors]

        coffee_scores = []
        for coffee in coffees:
            coffee_flavors = coffee.com.replace(' ', '').split('、')
            score = sum(flavor in coffee_flavors for flavor in selected_flavors_jp if flavor)
            if score > 0:  # スコアが0より大きい場合のみ結果に含める
                coffee_scores.append({
                    'name': coffee.co_name,
                    'score': score,
                    'image': settings.STATIC_URL + 'img/' + coffee.three_letters.lower() + '.png'
                })

        # スコアでソート
        coffee_scores.sort(key=lambda x: x['score'], reverse=True)

        return JsonResponse({
            'top_coffees': coffee_scores[:3],  # トップ3のみ返却
        })

    return render(request, 'authtest/home.html')
