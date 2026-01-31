import streamlit as st
import time

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 针对手机端“按钮不居中”和“输入框太扁”的暴力修复 CSS ---
st.markdown("""
    <style>
    /* 1. 全局背景：粉色渐变 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%) !important;
        background-attachment: fixed !important;
        font-family: "Microsoft YaHei", sans-serif !important;
    }

    /* 2. 隐藏 Streamlit 自带的无关元素 (红条、菜单) */
    header, footer, .viewerBadge_container__1QSob {
        display: none !important;
        visibility: hidden !important;
    }

    /* 3. 核心卡片容器：手机端适配 */
    .block-container {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 30px !important;
        padding: 2.5rem 1.5rem !important;
        margin-top: 50px !important; /* 距离顶部留出空间 */
        box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important;
        max-width: 420px !important;
    }

    /* === 手机端特殊调整 === */
    @media only screen and (max-width: 600px) {
        .block-container {
            width: 92% !important; /* 手机上卡片宽度 */
            margin-top: 30px !important;
            padding: 2rem 1.2rem !important;
        }
    }

    /* 4. 标题样式 */
    h1 {
        color: #ff8e9e !important;
        text-align: center !important;
        font-weight: 800 !important;
        font-size: 26px !important;
        margin-bottom: 5px !important;
    }
    
    .subtitle {
        text-align: center;
        color: #a4b0be;
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* 5. 修复输入框：增加高度，垂直居中 */
    div[data-testid="stTextInput"] {
        margin-top: 0px !important;
    }
    
    div[data-testid="stTextInput"] input {
        border-radius: 50px !important;
        border: 2px solid #ffcccc !important;
        background-color: #fff !important;
        
        /* 核心修复：高度不够的问题 */
        height: 60px !important;  /* 强制增高到 60px */
        line-height: 60px !important; /* 保证文字垂直居中 */
        
        text-align: center !important;
        font-size: 18px !important;
        color: #555 !important;
        padding: 0 20px !important; /* 左右留白 */
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81 !important;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3) !important;
    }

    /* 6. 核心修复：按钮居中 + 变宽 */
    
    /* 第一步：让按钮的外层容器占满宽度，并居中对齐 */
    .stButton {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        margin-top: 20px !important;
    }
    
    /* 第二步：让按钮本身占满容器，实现“横向长条”效果 */
    div.stButton > button {
        width: 100% !important; 
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        height: 60px !important; /* 按钮高度也设为 60px，与输入框一致 */
        border: none !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 8px 20px rgba(255, 154, 158, 0.4) !important;
        padding: 0 !important;
    }
    
    div.stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 结果展示卡片 */
    .result-card {
        background: #FFF0F5;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        color: #555;
        border: 2px dashed #ffb7c5;
        margin-top: 25px;
        animation: fadeIn 0.8s;
    }
    @keyframes fadeIn {from {opacity:0; transform:translateY(10px);} to {opacity:1; transform:translateY(0);}}
    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 界面内容 ---

# 标题区域
st.markdown("<h1>🐰 期末成绩查询</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>请输入手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 查询按钮
if st.button("✨ 查 询 ✨"):
    if not phone_input:
        st.warning("⚠️ 还没输入手机号哦")
    elif phone_input in student_database:
        # 模拟加载
        with st.spinner('🐰 正在查找...'):
            time.sleep(0.5)
        
        data = student_database[phone_input]
        
        # 结果展示区
        st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#ff6b81; margin:0 0 10px 0;">🎉 找到啦: {data['name']}</h3>
                <div style="font-size: 16px; line-height: 1.8;">{data['scores']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("🚫 没找到这个号码")

# 底部版权
st.markdown("<div style='text-align: center; color: #fff; margin-top: 50px; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师的成绩魔法屋</div>", unsafe_allow_html=True)
