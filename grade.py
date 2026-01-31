import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 暴力适配 CSS (解决手机显示错乱的核心) ---
st.markdown("""
    <style>
    /* 强制重置网页字体颜色，防止手机夜间模式导致“白字白底”看不清 */
    body, .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        background-attachment: fixed;
        font-family: "Microsoft YaHei", sans-serif !important;
        color: #333333 !important; /* 强制字体变黑 */
    }

    /* === 核心卡片容器 === */
    .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        padding: 1.5rem !important; /* 减小内边距 */
        margin-top: 0px !important;
        max-width: 450px;
    }

    /* === 📱 手机端究极适配 === */
    @media only screen and (max-width: 600px) {
        .block-container {
            padding: 1rem !important;
            padding-top: 2rem !important; /* 顶部稍微留点空隙防刘海屏 */
        }
        
        /* 强制隐藏右上角的汉堡菜单和 footer，防止遮挡 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 调整标题大小 */
        h1 { font-size: 22px !important; margin-bottom: 10px !important; }
        
        /* 输入框变大，方便按 */
        div[data-testid="stTextInput"] input {
            font-size: 18px !important; 
            height: 55px !important;
            color: #333 !important; /* 强制输入文字黑色 */
            background-color: #fff !important; /* 强制背景白色 */
        }
    }

    /* === 标题样式 === */
    h1 {
        color: #ff6b81 !important;
        text-align: center;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        padding: 0;
        font-size: 26px;
    }

    /* === 输入框美化 === */
    div[data-testid="stTextInput"] input {
        border-radius: 50px;
        border: 2px solid #ffcccc;
        text-align: center;
        height: 50px;
        font-size: 16px;
        color: #333;
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81;
        box-shadow: 0 0 8px rgba(255, 107, 129, 0.3);
    }

    /* === 按钮美化 === */
    div.stButton > button {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%);
        color: white !important; /* 按钮文字必须白 */
        border-radius: 50px;
        height: 55px;
        width: 100%;
        border: none;
        font-size: 18px;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0 4px 10px rgba(255, 154, 158, 0.3);
    }

    /* === 结果框样式 === */
    .result-box {
        background-color: #FFF0F5;
        border: 2px dashed #ffb7c5;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-top: 25px;
        color: #555 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面布局 ---
st.markdown("<h1>凯文老师的<br>✨成绩魔法屋✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #999; margin-bottom: 20px; font-size: 14px;'>👇 请输入家长手机号查询</p>", unsafe_allow_html=True)

phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

if st.button("🚀 点击查询"):
    if not phone_input:
        st.warning("⚠️ 请输入手机号")
    elif phone_input in student_database:
        with st.spinner('🐰 查询中...'):
            time.sleep(0.5)
        data = student_database[phone_input]
        st.markdown(f"""
            <div class="result-box">
                <h3 style="color: #ff6b81; margin: 0 0 10px 0;">🎉 学员：{data['name']}</h3>
                <div style="font-size: 16px; line-height: 1.6; color: #555;">
                    <strong>📝 成绩详情：</strong><br>
                    {data['scores']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 未找到该号码")

# 底部留白，防止手机底部遮挡
st.write("")
st.write("")
st.markdown("<div style='text-align: center; color: #fff; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师专属系统</div>", unsafe_allow_html=True)
