from django.shortcuts import render
from .models import Coffee

def home(request):
    coffees = Coffee.objects.all()
    if request.method == 'POST':
        # フォームから送られてきたデータを取得
        selected_flavors = {
            'キャンディードシトラス': request.POST.get('candied_citrus', False),
            'スイートシトラス': request.POST.get('sweet_citrus', False),
            'グレープフルーツ': request.POST.get('grapefruit', False),
            'レモン': request.POST.get('remon', False),
            'オレンジ': request.POST.get('orange', False),
            'ミルクチョコレート': request.POST.get('milk_chocolate', False),
            'ダークチョコレート': request.POST.get('dark_chocolate', False),
            'チョコレート': request.POST.get('chocolate', False),
            'ココア': request.POST.get('cocoa', False),
            'シナモン': request.POST.get('cinnamon', False),
            'スパイス': request.POST.get('spice', False),
            'ハーブ': request.POST.get('herb', False),
            'リンゴ': request.POST.get('apple', False),
            'ブルーベリー': request.POST.get('blueberry', False),
            'ベリー類': request.POST.get('berry', False),
            'レーズン': request.POST.get('raisin', False),
            'ナッツ': request.POST.get('nuts', False),
            '煎ったナッツ': request.POST.get('roasted_nuts', False),
            'ピーカンナッツ': request.POST.get('pecan_nuts', False),
            'ローストした野菜': request.POST.get('roasted_veg', False),
            'カラメル': request.POST.get('caramel', False),
            'チーズ': request.POST.get('cheese', False),
            'トフィー': request.POST.get('toffee', False),
            'バター': request.POST.get('better', False),
            'メープル': request.POST.get('maple', False),
            'オートミール': request.POST.get('oatmeal', False),
            'カラント(スグリ)': request.POST.get('currant', False),
            'キャラメル': request.POST.get('caramel2', False),
        }
        '''
        # コーヒーのスコアを計算
        coffee_scores = {}
        for coffee in coffees:
            score = 0
            for flavor in selected_flavors:
                if flavor in coffee.com:
                    score += 1
            coffee_scores[coffee.co_name] = score
        '''
        selected_flavors = request.POST.getlist('flavor')  # 正しく複数の値を取得するためにgetlistを使用
        # コーヒーのスコアを計算
        coffee_scores = {}
        for coffee in coffees:
            score = sum(flavor in coffee.com for flavor in selected_flavors)
            coffee_scores[coffee.co_name] = score

        # スコアが高い順にソート
        sorted_coffees = sorted(coffee_scores.items(), key=lambda x: x[1], reverse=True)

        # 上位3つのコーヒーを取得
        top_coffees = sorted_coffees[:3]

        # それぞれのコーヒーに対応する画像を取得
        coffee_images = {
            'スターバックスライトノートブレンド': 'static/img/lnb.png',
            'ブレックファーストブレンド'       : 'static/img/brk.png',
            'サイレンブレンド'                : 'static/img/srn.png',
            'ケニア'                         : 'static/img/ken.png',
            'パイクプレイスロースト'           : 'static/img/edb.png',
            'グアテマラアンティグア'           : 'static/img/gua.png',
            'エチオピア'                      : 'static/img/bna.png',
            'ハウスブレンド'                  : 'static/img/hou.png',
            'ディカフェハウスブレンド'         : 'static/img/dho.png',
            'コロンビア'                      : 'static/img/clg.png',
            'トウキョウロースト'               : 'static/img/tyo.png',
            'スマトラ'                        : 'static/img/sum.png',
            'コモドドラゴンブレンド'           : 'static/img/kdr.png',
            'カフェベロナ'                    : 'static/img/ver.png',
            'エスプレッソロースト'             : 'static/img/esp.png',
            'イタリアンロースト'               : 'static/img/ita.png',
            'フレンチロースト'                 : 'static/img/fre.png',
        }
        
        # コンテキストに追加
        context = {
            'top_coffees': top_coffees,
            'coffee_images': coffee_images,
            'coffee_scores': coffee_scores,
        }
        return render(request, 'authtest/home.html', context)
    else:
        # GETリクエストの場合は空のコンテキストを渡す
        return render(request, 'authtest/home.html', {})

'''
ユーザーが好きな食事を入力
それをデータベースCOFFEEのcom(相性のいい風味)に出てくるキーワードに分類して
コーヒーの名前を提案する
該当しなければ該当なしと返す
提案されたコーヒーの詳細についても表示したい

homeの完成ページをhttps://www.starbucks.co.jp/index.htmlとhttps://pokemon-tools.netlify.app/speed-checker/を混ぜたようなデザインにしたいです。サイトの色は一つ目を参考に、ボタンの配置や使い方は２つ目を参考にしたいです。商用ではないので、スターバックスのロゴを使いたいです。
機能の説明です。
home.htmlにて２つ目のＵＲＬのようなレイアウトで、「フードを入力」という欄に入力します。（例えばプリン）そのあとその下に「それはオレンジっぽい？」という欄があり「はい」、「いいえ」を選べます。このような質問をCOFFEE.csvのcomに出てくるフードの分聞くようにします。これはどのワードが一番「はい」なのかを知るためのものです。そして「検索」と押すと「〇〇は△△と相性がいいです。」と出力します。（〇〇はユーザーが入力したフードの名前で、△△はCOFFEE.csvのco_nameです。）メカニズムは「はい」の数によってポイントを獲得するようにします。例えば「それはオレンジっぽい？」に「はい」、「それはレモンっぽい？」に「はい」と答えたら「オレンジ」と「レモン」に１ポイント獲得させます。
そして、COFFEE.csvのデータを参考にコーヒーごとに得たポイントを合算します。例えば先ほどの例ですと、オレンジとレモンにそれぞれ1ポイント入ってるので、スターバックスウィローブレンドは2ポイント獲得したことになります。なぜならスターバックスウィローブレンドのcomにはオレンジとレモンという項目があるからです。（「1,スターバックスウィローブレンド,軽,高,オレンジ、レモン,WLB」を参照）
このようにして「それはオレンジっぽい？」のような質問に答えてcomに登場してる名前ごとに1か0のポイントを振り、それをコーヒーごとに合算します。その合計が最も多いものを出力するというシステムです。この時、最も多いのが複数あった場合、一番多いポイントのコーヒーを全て出力します。また、すべてコーヒーのポイントが０だった場合、「〇〇は△△と相性がいいです。」と出力するのではなく、「お探しのコーヒーは見当たりませんでした。」と出力します。

このような機能を持ったものをhome.htmlに実装し、cssとjsも併せて実装したいです。

貴方がぞれぞれのファイルの内容を編集し、私に一度提案してください。
それを私が実装し、動かしてフィードバックします。
では、コードを書いてください。
また、私のアイデアに改善案や強化した方がいい箇所がありましたら、言ってください。
'''
