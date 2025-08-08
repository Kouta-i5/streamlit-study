import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import time

st.set_page_config(
    page_title="Streamlit入門テンプレート",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("ナビゲーション")
page = st.sidebar.radio(
    "ページを選択してください:",
    ["テキスト表示", "メディア", "インタラクティブ機能", "データ入出力"]
)

st.title("Streamlit入門テンプレートアプリ")
st.markdown("---")

if page == "テキスト表示":
    st.header("1. テキスト表示機能")
    st.title('streamlit Tutorial')
    # ヘッダ
    st.header('This is a header')
    # サブヘッダ
    st.subheader('This is a subheader')
    # テキスト
    st.text('Hello World!')
    # st.write()はMarkdown表記対応
    st.write('# headline1')
    # 以下のように明示的に書くことも可能
    st.markdown('# headline2')
    # ファイルアップロード
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write(uploaded_file)
    # ボタンの設置 
    if st.button('Say hello'):
        st.write('Hello World!')
    # チェックボックスの設置   
    if st.checkbox('Show/Hide'):
        st.write('Some text')
    # ラジオボタンの設置
    option = st.radio('Which number do you like best?', ['1', '2', '3'])
    # セレクトボックスの設置
    option = st.selectbox('Which number do you like best?', ['1', '2', '3'])
    # テキスト入力ボックス
    text_input = st.text_input('Input', 'Input some text here.')
    # テキストエリア
    text_area = st.text_area('Text Area', 'Input some text here.') 

elif page == "メディア":
    st.header("2. メディア表示機能")
    
    # 画像表示
    st.subheader("2.1 画像の表示")
    st.write("ローカルの画像またはURLから画像を表示できます")
    
    # サンプル画像のURLを使用
    image_url = "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
    st.image(image_url, caption="Streamlitのロゴ", width=300)
    
    st.code("""
    # 画像を表示するコード
    image_url = "https://example.com/image.jpg"
    st.image(image_url, caption="画像の説明", width=300)
    
    # または、ローカルの画像を使用する場合
    from PIL import Image
    img = Image.open("local_image.jpg")
    st.image(img, caption="ローカル画像", width=300)
    """, language="python")
    
    # 動画表示
    st.subheader("2.2 動画の表示")
    st.write("YouTube動画を埋め込むことができます")
    st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
    
    st.code("""
    # 動画を表示するコード
    st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
    
    # または、ローカルの動画ファイルを使用する場合
    video_file = open("my_video.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    """, language="python")
    
    # オーディオ
    st.subheader("2.3 オーディオの表示")
    st.write("オーディオファイルを再生できます（ローカルファイルの例）")
    st.code("""
    # オーディオを表示するコード（実行時はコメントを外してください）
    # audio_file = open("my_audio.mp3", "rb")
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format="audio/mp3")
    """, language="python")

elif page == "インタラクティブ機能":
    st.header("3. インタラクティブ機能")
    
    # ボタン
    st.subheader("3.1 ボタン")
    if st.button("クリックしてください"):
        st.write("ボタンがクリックされました！")
    
    # チェックボックス
    st.subheader("3.2 チェックボックス")
    show_text = st.checkbox("テキストを表示する")
    if show_text:
        st.write("チェックボックスがオンになりました！")
    
    # ラジオボタン
    st.subheader("3.3 ラジオボタン")
    animal = st.radio(
        "好きな動物を選んでください:",
        ["犬", "猫", "うさぎ"]
    )
    st.write(f"あなたは{animal}を選びました。")
    
    # セレクトボックス
    st.subheader("3.4 セレクトボックス")
    option = st.selectbox(
        "好きなプログラミング言語を選んでください:",
        ["Python", "JavaScript", "Java", "C++", "Go"]
    )
    st.write(f"あなたは{option}を選びました。")
    
    # マルチセレクト
    st.subheader("3.5 マルチセレクト")
    options = st.multiselect(
        "好きな色を選んでください（複数選択可）:",
        ["赤", "青", "緑", "黄", "紫"],
        ["青"]
    )
    st.write(f"選択された色: {', '.join(options)}")
    
    # スライダー
    st.subheader("3.6 スライダー")
    age = st.slider("年齢を選択してください:", 0, 100, 25)
    st.write(f"選択された年齢: {age}")
    
    # テキスト入力
    st.subheader("3.7 テキスト入力")
    name = st.text_input("あなたの名前を入力してください:")
    if name:
        st.write(f"こんにちは、{name}さん！")
    
    # テキストエリア
    st.subheader("3.8 テキストエリア")
    message = st.text_area("メッセージを入力してください:")
    if message:
        st.write(f"入力されたメッセージ: {message}")
    
    # 日付入力
    st.subheader("3.9 日付選択")
    date = st.date_input("日付を選択してください:")
    st.write(f"選択された日付: {date}")
    
    # 時間入力
    st.subheader("3.10 時間選択")
    time_val = st.time_input("時間を選択してください:")
    st.write(f"選択された時間: {time_val}")
    
    # ファイルアップロード
    st.subheader("3.11 ファイルアップロード")
    uploaded_file = st.file_uploader("ファイルをアップロードしてください:", type=["csv", "txt", "jpg", "png"])
    if uploaded_file is not None:
        st.write(f"ファイル名: {uploaded_file.name}")
        # ファイルの種類に応じた処理（例：CSVならデータフレーム表示）
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.write("データプレビュー:")
            st.dataframe(df.head())
    
    # プログレスバー
    st.subheader("3.12 プログレスバー")
    if st.button("プログレスバーを表示"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)  # 実際のアプリでは実行時間がかかる処理
            progress_bar.progress(i + 1)
        st.success("完了しました！")

elif page == "データ入出力":
    st.header("4. データ入出力機能")
    
    # データフレームの作成と表示
    st.subheader("4.1 データフレームの表示")
    df = pd.DataFrame({
        '名前': ['太郎', '花子', '一郎', '京子', '健太'],
        '年齢': [25, 30, 45, 22, 35],
        '都道府県': ['東京', '大阪', '福岡', '北海道', '愛知'],
        '得点': [85, 92, 78, 96, 88]
    })
    
    st.write("基本的なデータフレーム表示:")
    st.dataframe(df)
    
    st.write("静的なテーブルとして表示:")
    st.table(df)
    
    # メトリクス表示
    st.subheader("4.2 メトリクスの表示")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="平均得点", value=f"{df['得点'].mean():.1f}", delta="4.2")
    with col2:
        st.metric(label="最高得点", value=f"{df['得点'].max()}", delta="2.0")
    with col3:
        st.metric(label="最低得点", value=f"{df['得点'].min()}", delta="-1.5")
    
    # グラフ作成（Matplotlib）
    st.subheader("4.3 Matplotlibでグラフ作成")
    fig, ax = plt.subplots()
    ax.bar(df['名前'], df['得点'])
    ax.set_title('得点グラフ')
    ax.set_ylabel('得点')
    st.pyplot(fig)
    
    # グラフ作成（Plotly）
    st.subheader("4.4 Plotlyでのインタラクティブなグラフ")
    fig = px.bar(df, x='名前', y='得点', color='都道府県', title='都道府県別得点')
    st.plotly_chart(fig)
    
    # 折れ線グラフ（Plotly）
    st.subheader("4.5 時系列データの折れ線グラフ")
    # サンプル時系列データの作成
    date_range = pd.date_range(start='2023-01-01', periods=30, freq='D')
    time_data = pd.DataFrame({
        '日付': date_range,
        '売上': np.random.randint(100, 500, size=30),
        'アクセス数': np.random.randint(1000, 5000, size=30)
    })
    
    fig = px.line(time_data, x='日付', y=['売上', 'アクセス数'], title='日別の売上とアクセス数')
    st.plotly_chart(fig)
    
    # CSV出力
    st.subheader("4.6 CSVファイルのダウンロード")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="サンプルデータをCSVでダウンロード",
        data=csv,
        file_name='sample_data.csv',
        mime='text/csv',
    )
    
    # JSONデータの表示
    st.subheader("4.7 JSONデータの表示")
    st.json({
        'name': '山田太郎',
        'age': 30,
        'address': {
            'city': '東京',
            'zip': '100-0001'
        },
        'interests': ['プログラミング', '読書', '旅行']
    })
    
    # キャッシュの使用例
    st.subheader("4.8 データのキャッシュ")
    st.write("@st.cacheデコレータを使用して、重い計算やデータロードをキャッシュできます")
    st.code("""
    @st.cache_data
    def load_data():
        # 時間のかかる処理（例：大きなCSVファイルの読み込み）
        df = pd.read_csv("large_file.csv")
        return df
    
    # キャッシュされたデータを使用
    data = load_data()  # 2回目以降の呼び出しは高速
    """, language="python")
    
    # セッション状態の例
    st.subheader("4.9 セッション状態の保存")
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    
    st.write(f"現在のカウンター: {st.session_state.counter}")
    
    if st.button("カウンターを増やす"):
        st.session_state.counter += 1
        st.experimental_rerun()  # 画面を更新
# フッター
st.markdown("---")
st.markdown("### Streamlit入門テンプレートアプリ")
st.markdown("このアプリはStreamlitの基本機能を紹介するためのテンプレートです。")