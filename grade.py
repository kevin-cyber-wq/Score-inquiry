import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 暴力 CSS (针对组件内部样式的深度定制) ---
st.markdown("""
    <style>
    /* 全局背景 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%) !important;
        background-attachment: fixed !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }
    
    /* 隐藏无关元素 */
    header, footer, .viewerBadge_container__1QSob { display: none !important; }

    /* 卡片容器适配 */
    .block-container {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 30px !important;
        padding: 2rem 1.5rem !important;
        margin-top: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important;
        max-width: 420px !important;
    }
    @media only screen and (max-width: 600px) {
        .block-container {
            width: 92% !important;
            margin-top: 20px !important;
            padding: 2rem 1rem !important;
        }
    }

    /* 标题 */
    h1 {
        color: #ff8e9e !important;
        text-align: center !important;
        font-size: 26px !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }

    /* === 修复输入框高度 (Target data-baseweb) === */
    /* Streamlit 的输入框很复杂，必须针对这个 baseweb 属性修改才生效 */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #ffcccc !important;
        background-color: #fff !important;
        height: 60px !important;  /* 强制增高外框 */
        padding: 0 15px !important;
    }
    
    /* 内部输入的文字 */
    div[data-baseweb="input"] input {
        text-align: center !important;
        font-size: 18px !important;
        color: #555 !important;
        height: 100% !important;
        margin-top: 2px !important; /* 微调文字垂直位置 */
    }
    
    /* 选中状态 */
    div[data-baseweb="input"]:focus-within {
        border-color: #ff6b81 !important;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3) !important;
    }

    /* === 修复按钮 (配合 Python columns 使用) === */
    div.stButton > button {
        width: 100% !important;  /* 填满所在的列 */
        height: 60px !important; /* 高度与输入框一致 */
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 8px 15px rgba(255, 154, 158, 0.4) !important;
        padding: 0 !important;
    }
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 结果卡片 */
    .result-card {
        background: #FFF0F5;
        border: 2px dashed #ffb7c5;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-top: 25px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面逻辑 ---
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ccc; font-size:14px; margin-bottom:15px;'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 增加一点间距
st.write("")

# === 🔥 核心修改：使用 Columns 布局强制居中 🔥 ===
# 我们创建3列：[空, 中间内容, 空]。中间列占 90% 宽度，左右留一点点白
# 这样按钮就被强制关在了“中间列”里，想跑偏都跑不了！
col1, col2, col3 = st.columns([0.05, 0.9, 0.05])

with col2:
    search_btn = st.button("✨ 查 询 ✨")

if search_btn:
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        data = student_database[phone_input]
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0 0 10px 0;">🎉 找到啦: {data['name']}</h3>
                <div style="font-size:16px; line-height:1.8;">{data['scores']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

st.markdown("<div style='text-align: center; color: #fff; margin-top: 50px; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)
