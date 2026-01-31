import streamlit as st
import time

# --- 1. 页面基础设置 (手机端适配关键) ---
st.set_page_config(
    page_title="✨ 凯文老师的成绩魔法屋 ✨", 
    page_icon="🐰", 
    layout="centered",
    initial_sidebar_state="collapsed" # 默认收起侧边栏，手机上看更清爽
)

# --- 2. 🎨 移动端适配 CSS 魔法 ---
st.markdown("""
    <style>
    /* 全局背景：柔和的莫兰迪粉渐变 */
    .stApp {
        background-image: linear-gradient(120deg, #fccb90 0%, #d57eeb 100%);
        font-family: "Microsoft YaHei", sans-serif;
    }
    
    /* === 核心卡片容器设计 === */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        padding: 2rem 1rem !important; /* 减小内边距，手机屏占比更高 */
    }

    /* === 📱 手机端专属优化 (重点) === */
    /* 当屏幕宽度小于 600px (手机) 时，强制调整布局 */
    @media only screen and (max-width: 600px) {
        .main .block-container {
            width: 95% !important;        /* 宽度占满屏幕 */
            padding: 1.5rem 1rem !important; 
            margin-top: -50px !important; /* 去除 Streamlit
