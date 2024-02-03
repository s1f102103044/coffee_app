from django.shortcuts import render
from .models import Coffee
from .forms import FoodForm

def recommend_coffee(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.cleaned_data['food']
            recommended_coffees = Coffee.objects.filter(com__icontains=food)
            return render(request, 'recommendations.html', {'coffees': recommended_coffees, 'food': food})
    else:
        form = FoodForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    query = request.GET.get('q', '')  # qパラメータから検索語句を取得
    if query:
        # 検索語句に基づいてCoffeeテーブルを検索
        coffees = Coffee.objects.filter(name__icontains=query)
    else:
        coffees = Coffee.objects.all()  # 何も検索されていなければ全てのレコードを取得

    return render(request, 'home.html', {'coffees': coffees, 'query': query})

'''
ユーザーが好きな食事を入力
それをデータベースCOFFEEのcom(相性のいい風味)に出てくるキーワードに分類して
コーヒーの名前を提案する
該当しなければ該当なしと返す
提案されたコーヒーの詳細についても表示したい

手順
1.CSVファイルを作成、インポート(やり方は調べる)
2.
'''
