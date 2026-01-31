import streamlit as st
import time

# --- 1. 页面配置 (浏览器标签页标题) ---
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 深度定制 CSS (手机端适配核心) ---
st.markdown("""
    <style>
    /* === 全局背景：粉紫渐变 === */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        background-attachment: fixed; /* 背景固定，防止滚动时出现白边 */
        font-family: "Microsoft YaHei", sans-serif;
    }

    /* === 核心卡片容器 (模仿 HTML 的 .card) === */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        padding: 2rem;
        max-width: 450px; /* 电脑上限宽，模拟手机比例 */
        margin-top: 20px;
    }

    /* === 📱 重点：手机端强制适配 === */
    @media only screen and (max-width: 600px) {
        .main .block-container {
            width: 95% !important;       /* 手机上宽度占满 */
            padding: 1.5rem 1rem !important; /* 减小内边距 */
            margin-top: 0px !important;  /* 去除顶部留白 */
        }
        
        /* 手机上标题字号调整 */
        h1 { font-size: 24px !important; }
        
        /* 手机上输入框高度增加，防止点不到 */
        div[data-testid="stTextInput"] input {
            height: 55px !important;
            font-size: 18px !important; /*防止iPhone自动缩放*/
        }
    }

    /* === 标题样式 === */
    h1 {
        color: #ff6b81 !important;
        text-align: center;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        padding: 0;
        margin-bottom: 10px;
        font-size: 28px;
        line-height: 1.4;
    }

    /* === 输入框美化 === */
    div[data-testid="stTextInput"] input {
        border-radius: 50px;
        border: 2px solid #ffcccc;
        text-align: center;
        height: 50px;
        font-size: 18px;
        color: #555;
        transition: all 0.3s;
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3);
    }

    /* === 按钮美化 === */
    div.stButton > button {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 100%);
        color: white;
        border-radius: 50px;
        height: 55px;
        width: 100%;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4);
        margin-top: 10px;
    }
    
    div.stButton > button:active {
        transform: scale(0.98);
    }

    /* === 隐藏多余元素 === */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* === 结果展示框样式 === */
    .result-box {
        background-color: #FFF0F5;
        border: 2px dashed #ffb7c5;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-top: 20px;
        color: #555;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {from {opacity:0; transform:translateY(10px);} to {opacity:1; transform:translateY(0);}}
    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据库 ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 页面布局 ---

# 页面标题
st.markdown("<h1>凯文老师的<br>✨成绩魔法屋✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a4b0be; margin-bottom: 25px; font-size: 14px;'>👇 请输入预留手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

st.write("") # 增加一点空隙

# 查询按钮
if st.button("🚀 点击查询"):
    if not phone_input:
        st.warning("⚠️ 哎呀，还没输入手机号呢！")
    
    elif phone_input in student_database:
        # 模拟加载效果
        with st.spinner('🐰 正在翻阅成绩单...'):
            time.sleep(0.6)
        
        data = student_database[phone_input]
        
        # 显示结果 (使用HTML渲染，保证手机上好看)
        st.markdown(f"""
            <div class="result-box">
                <h3 style="color: #ff6b81; margin: 0 0 10px 0;">🎉 学员：{data['name']}</h3>
                <div style="font-size: 16px; line-height: 1.6;">
                    <strong>📝 成绩详情：</strong><br>
                    {data['scores']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        
    else:
        st.error("🚫 暂无记录\n请检查手机号是否输入正确。")

# 底部版权
st.markdown("<div style='text-align: center; margin-top: 40px; color: #fff; opacity: 0.8; font-size: 12px;'>☁️ 凯文老师专属查询系统</div>", unsafe_allow_html=True)
