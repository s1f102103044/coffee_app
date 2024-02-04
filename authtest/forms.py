# forms.py

from django import forms

FLAVOR_CHOICES = [
    ('citrus', 'シトラス系'),
    ('chocolate', 'チョコレート系'),
    ('spice', 'スパイス系'),
    ('fruit', 'フルーツ系'),
    ('nuts', 'ナッツ系'),
    ('other', 'その他'),
]

class FlavorForm(forms.Form):
    flavor = forms.MultipleChoiceField(
        choices=FLAVOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='フレーバー'
    )

'''
28品目
・オレンジ
・レモン
・ミルクチョコレート
・煎ったナッツ
・ナッツ
・リンゴ
・ブルーベリー
・キャンディードシトラス
・チョコレート
・グレープフルーツ
・ベリー類
・カラント（スグリ）
・シナモン
・キャラメル
・ダークチョコレート
・スイートシトラス
・ピーカンナッツ
・レーズン
・オートミール
・ココア
・メープル
・バター
・トフィー
・チーズ
・ハーブ
・カラメル
・スパイス
・ローストした野菜
'''