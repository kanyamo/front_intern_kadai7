# コードレビュー

このコードレビューは、ブランチ `matsumoto-kota` に対してのレビューです。
新たにブランチ `matsumoto-kota-review` を作成し、改善点を修正したうえでその改善点をレビューさせていただきました

## 総評

- 問題ないと思います
- バグも触ってみたところなく、機能も問題なく動いているように見えます
- base.htmlを継承したテンプレートの作成やページネーション、Djangoのフォームの使い方など、Djangoのフロントエンドの基本的な使い方を理解していると思います


## HTMLについて

- テンプレートの継承(extends, block)がうまく使えています。base.htmlを継承したテンプレートを作成しているのは良いですね
- ページネーションがうまく使えています。ページネーションの実装は難しいので、これはすごいです
- サイドバーの各メニューなどは、テンプレートの挿入タグ(include)を使うとさらに変更に強いコードを書くことができます。例えば、以下のように書くことができます

```html
<!-- base.html -->
{% url 'todo:calendar' as calendar_url %}
{% url 'todo:index' as todo_url %}
{% url 'todo:chart' as chart_url %}
<div class="menu-content">
    {% include 'todo/sidebar.html' with menu_name='Calendar' icon_name='calendar.svg' selected=request.path == calendar_url %}
    {% include 'todo/sidebar.html' with menu_name='Todo' icon_name='todo.svg' selected=request.path == todo_url %}
    {% include 'todo/sidebar.html' with menu_name='Chart' icon_name='chart.svg' selected=request.path == chart_url %}
    <div class="menu-settings">
        <img src="{% static 'todo/img/settings.svg' %}">
    </div>
</div>
```

```html
<!-- sidebar.html -->
<div class="menu-element{% if selected %} selected{% endif %}">
    <img src="{% static 'todo/img/{{ icon_name }}' %}">
    <p>{{ menu_name }}</p>
</div>
```

ここで、 `selected` クラスを付与するかどうかは、現在のページのURLが、そのメニューのURLと一致するかどうかで判断しています。これは、 `request.path` という変数に、現在のページのURLが入っているので、それを使っています。JSで付け替えるのもひとつの方法ですが、Djangoのテンプレート言語を使うと上記のような書き方もできます。

- 日時を表す部分で、Djangoのテンプレートフィルターが使えていて素晴らしいです。
- さらに、このようなときは、 `time` タグを使うと、より意味のあるHTMLを書くことができます。以下はコード例です

```html
<time datetime="{{ todo.deadline_date | date:'c' }}T{{ todo.deadline_time | date:'c'}}" class="deadline">
    {{ todo.deadline_date | date:"n/j(D) " }}
    {{ todo.deadline_time | date:"H:i"}}
</time>
```

## CSSについて

- 課題概要の画像とほぼ同じ見た目が再現できています。
- CSSのクラス名がHTMLの構造を反映していて、わかりやすいです。
- クラスセレクタを基本とした、衝突しにくいCSSの書き方をしています。これは良いですね。
- htmlファイルに合わせてCSSファイルを分割しているのも良いですね。


## JSについて

- JSのコードを入れる部分がHTMLの最後になっていて、読み込みの速さも意識できています。
- さらに、テンプレート別にJSファイルが適用できるよう、 `block scripts` で囲っているところが堅牢ですね。
- 今回のコードは、クラスを付け替えるだけなので、前述したように、Djangoのテンプレート言語を使ってHTMLの構造を変える方法もあります。ただ、JSで書いているのも問題ないと思います。


# その他

- ファイルの最後の行は空行にしておくのが一般的です。もし、空行がないと、ファイルの最後の行が変更されたときに、gitのdiffが変な表示になってしまいます
- もしフォーマッタが使えるなら、フォーマッタを使うと、コードのフォーマットを統一することができます。
