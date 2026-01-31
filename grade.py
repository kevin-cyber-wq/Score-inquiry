import streamlit as st
import time

# --- 1. 页面基础配置 ---
# 这里设置了浏览器标签页显示的标题和图标
st.set_page_config(
    page_title="凯文老师的✨成绩魔法屋✨", 
    page_icon="🐰", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 深度定制 CSS (核心美化部分) ---
# 这段代码将 Streamlit 的默认样式完全覆盖，使其看起来像一个原生 APP
st.markdown("""
    <style>
    /* 1. 全局背景：完全还原 HTML 版的粉紫渐变 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        background-attachment: fixed;
        font-family: "Microsoft YaHei", "Heiti SC", sans-serif;
    }

    /* 2. 核心卡片容器：模拟 HTML 的 .card 样式 */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95); /* 半透明白底 */
        border-radius: 25px;       /* 大圆角 */
        box-shadow: 0 10px 30px rgba(0,0,0,0.15); /* 阴影浮起感 */
        padding: 2.5rem 2rem !important;
        max-width: 450px;          /* 限制电脑端最大宽度，像手机界面 */
        margin-top: 30px;
    }

    /* === 📱 手机端深度适配 (Media Queries) === */
    @media only screen and (max-width: 600px) {
        .main .block-container {
            width: 92% !important;        /* 手机上几乎占满宽度 */
            padding: 2rem 1rem !important;/* 减小内边距 */
            margin-top: 0px !important;   /* 顶格显示，不浪费空间 */
        }
        
        /* 手机上标题微调 */
        h1 { font-size: 24px !important; }
        
        /* 手机上结果卡片字体加大 */
        .result-card { font-size: 16px !important; }
    }

    /* 3. 标题样式 */
    h1 {
        color: #ff6b81 !important;
        text-align: center;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        padding-bottom: 0px;
        margin-bottom: 10px;
        font-size: 28px;
    }

    /* 4. 输入框美化：完全还原 HTML 的圆角边框 */
    div[data-testid="stTextInput"] input {
        border-radius: 50px;
        border: 2px solid #ffcccc;
        background-color: #fff;
        text-align: center;
        height: 55px;          /* 加高，手指好点 */
        font-size: 18px;
        color: #555;
        transition: 0.3s;
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #ff6b81;
        box-shadow: 0 0 10px rgba(255, 107, 129, 0.3);
    }

    /* 5. 按钮美化：粉色渐变 + 悬浮效果 */
    div.stButton > button {
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        color: white;
        border-radius: 50px;
        height: 60px;          /* 按钮做大一点 */
        width: 100%;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4);
        margin-top: 10px;
    }
    
    div.stButton > button:active {
        transform: scale(0.98); /* 点击时的按压感 */
    }

    /* 6. 隐藏 Streamlit 自带的无关元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 7. 结果展示区的样式 */
    .success-box {
        background-color: #fff0f6;
        border: 2px dashed #ffb7c5;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        color: #555;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 模拟数据库 (您可以随时修改这里) ---
student_database = {
    "13800138000": {"name": "小樱 🌸", "scores": "语文: 98 | 数学: 95 | 魔法: SS"},
    "13911112222": {"name": "鸣人 🍥", "scores": "忍术: 60 | 影分身: 100"},
    "123456": {"name": "测试宝宝 👶", "scores": "吃饭: 100 | 睡觉: 100"}
}

# --- 4. 页面内容布局 ---

# 标题与副标题
st.markdown("<h1>🐰 凯文老师的<br>✨成绩魔法屋✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a4b0be; margin-bottom: 25px;'>请输入预留手机号召唤成绩单</p>", unsafe_allow_html=True)

# 输入框 (隐藏了默认的 label，用 placeholder 提示)
phone_input = st.text_input("label", placeholder="在此输入手机号...", label_visibility="collapsed")

# 占位，增加一点间距
st.write("") 

# 查询按钮逻辑
if st.button("🚀 点击查询 🚀"):
    if not phone_input:
        st.warning("⚠️ 哎呀，还没有输入手机号哦！")
    
    elif phone_input in student_database:
        # 模拟数据加载动画
        with st.spinner('✨ 正在召唤数据...'):
            time.sleep(0.8)
        
        data = student_database[phone_input]
        
        # 使用 HTML 渲染结果，保证美观度
        st.markdown(f"""
            <div class="success-box">
                <h3 style="color: #ff6b81; margin: 0 0 10px 0;">🎉 找到学员：{data['name']}</h3>
                <div style="font-size: 16px; line-height: 1.8; color: #666;">
                    <strong>📝 期末成绩单：</strong><br>
                    {data['scores']}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons() # 撒花特效
        
    else:
        st.error("🚫 暂无记录\n请检查手机号是否输入正确。")

# 底部版权信息
st.markdown("<div style='text-align: center; margin-top: 50px; color: #fff; opacity: 0.6; font-size: 12px;'>☁️ 凯文老师专属查询系统</div>", unsafe_allow_html=True)
