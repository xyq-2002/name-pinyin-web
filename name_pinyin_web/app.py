import streamlit as st
from pypinyin import pinyin, Style

st.set_page_config(page_title="中文姓名转英文拼写", layout="wide")

st.title("中文姓名 → 英文拼写")

col1, col2 = st.columns(2)

def chinese_to_english(name):
    py = pinyin(name, style=Style.NORMAL, heteronym=False)
    result = "".join(item[0] for item in py)
    return result.capitalize()

with col1:
    input_text = st.text_area(
        "中文姓名（每行一个）",
        height=300,
        placeholder="张三\n李小龙\n王一博"
    )

with col2:
    if input_text:
        lines = input_text.splitlines()
        output = []
        for line in lines:
            line = line.strip()
            if line:
                output.append(chinese_to_english(line))
            else:
                output.append("")
        st.text_area(
            "英文拼写",
            value="\n".join(output),
            height=300
        )
    else:
        st.text_area("英文拼写", height=300)
