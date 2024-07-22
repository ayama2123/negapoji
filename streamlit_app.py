import streamlit as st
import openai
import os

# OpenAI APIキーを設定
openai.api_key = os.getenv('OPENAI_API_KEY')

def reframing(negative_word):
  prompt=f"""
  以下のネガティブな性格についてリフレーミングしてポジティブな解釈を教えてください。
  \n\nネガティブな性格: {text_input}\n\n
  また、このリフレーミングを踏まえた自己PRを作成し、長所と短所も含めてください。
  """
    response = openai.chat.completions.create(
      model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"自己PRを生成するGPTです。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

st.title("ネガポジ変換！自己PR作成マシン")
st.write("自分の性格を入力すると自己PRが作られます！")

negative_word = st.text_input("自分の性格を入力してください:")

if negative_word:
    with st.spinner("リフレーミング中..."):
        positive_reframe = reframing(negative_word)
        st.subheader("こんな解釈もできますね！")
        st.write(positive_reframe)
        
        # 長所と短所を自己PRとして出力
        st.subheader("自己PR")
        st.write(f"長所: {positive_reframe.split('and provide')[0].strip()}")
        st.write(f"短所: {negative_word}")
