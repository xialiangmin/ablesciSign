#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import requests

# Telegram 通知服务配置
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")  # 你的 Telegram Bot Token
TG_CHAT_ID = os.getenv("TG_CHAT_ID", "")      # 接收消息的 Chat ID

def telegram_bot(title: str, content: str):
    """Telegram 机器人通知"""
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        return
    
    print("Telegram 推送服务启动")
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    
    # 使用 HTML 格式拼接标题和内容，使标题加粗展示
    message_text = f"<b>{title}</b>\n\n{content}"
    
    data = {
        "chat_id": TG_CHAT_ID,
        "text": message_text,
        "parse_mode": "HTML",         # 允许使用简单的 HTML 标签格式化文本
        "disable_web_page_preview": True # 禁用链接预览（可选）
    }
    
    try:
        # 增加 timeout 防止网络阻塞
        response = requests.post(url, json=data, timeout=10)
        result = response.json()
        
        if result.get("ok"):
            print('Telegram 推送成功！')
        else:
            print(f"Telegram 推送失败: {result.get('description', '未知错误')}")
    except Exception as e:
        print(f"Telegram 推送异常: {str(e)}")

def send(title: str, content: str):
    """
    发送通知
    :param title: 通知标题
    :param content: 通知内容
    """
    print(f"通知标题: {title}")
    print(f"通知内容:\n{content}\n" + "-"*20)
    
    # 检查是否配置了必要的环境变量
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        print("未配置 Telegram 的 TOKEN 或 CHAT_ID 环境变量，跳过通知发送。")
        return

    # 发送 Telegram 通知
    telegram_bot(title, content)

if __name__ == '__main__':
    # 测试通知
    send("🚨 服务器警报", "这是一条来自 Python 脚本的 Telegram 测试通知消息。\n可以自由换行。")
