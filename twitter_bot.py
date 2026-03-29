import feedparser
import requests
import time

RSS_URL = "https://rsshub.app/twitter/user/granbluefantasy"
WEBHOOK_URL = "https://discord.com/api/webhooks/1480801568876924999/QHjRsrRTLHkSL3mz2xjUDMimVKXRbt4rRmSXK_6ypq7KRQcYkWay5DiaZyehoe18z6i4"

sent = set()

while True:
    feed = feedparser.parse(RSS_URL)

    for entry in feed.entries:
        if entry.link not in sent:
            data = {
                "content": f"📢 新しい投稿！\n{entry.link}"
            }
            requests.post(WEBHOOK_URL, json=data)
            sent.add(entry.link)

    time.sleep(60)  # 1分ごとチェック
