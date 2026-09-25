import csv
import os
import streamlit as st

# --- 1. CSVとCSSを読み込む関数 ---
def load_gal_data(query=""):
    results = []
    csv_file = 'gal_dict.csv'
    
    if not os.path.exists(csv_file):
        return results
        
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            word = row.get('word', '')
            meaning = row.get('meaning', '')
            example = row.get('example', '')
            
            # 部分一致で検索
            if not query or query.lower() in word.lower():
                results.append((word, meaning, example))
                
    return results

# --- 2. 画面のデザインとメイン処理 ---
def main():
    st.set_page_config(page_title="ガリ勉ギャル語事典", page_icon="💖", layout="centered")
    
    # CSSファイルの読み込み
    css_file = 'style.css'
    if os.path.exists(css_file):
        with open(css_file, mode='r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
    # タイトルエリア
    st.title("💖 ガリ勉ギャル語事典 💖")
    st.caption("SQLiteをPython＋Streamlitの技術に置き換えた、爆速検索ウェブシステム")
    
    # 検索窓
    search_query = st.text_input("", placeholder="調べたいギャル語を入力してね...（例：ぴえん）")
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    # データの取得と表示
    words = load_gal_data(search_query)
    
    if words:
        for word, meaning, example in words:
            # HTMLカスタムクラスを使ってCSSを適用
            st.markdown(f"""
            <div class='gal-card'>
                <div class='gal-word'>✨ {word}</div>
                <div class='gal-meaning'><strong>【意味】</strong> {meaning}</div>
                <div class='gal-example'>💡 <strong>使ってみた：</strong> 「{example}」</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("そのギャル語はまだ事典に登録されていないみたい…！")

if __name__ == "__main__":
    main()
