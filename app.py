# pip install line-bot-sdk flask pyquery

from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    StickerMessage,
    LocationMessage,
)

from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    StickerMessageContent,
    LocationMessageContent,
)

from modules.reply import faq, menu
from modules.taipeispot2 import get_taipeispot_table

import os

#specific_key = input("請輸入景點名稱:")
#print(get_taipeispot_table(specific_key))
#exit

app = Flask(__name__)

channel_secret = os.getenv("CHANNEL_SECRET")
channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")

configuration = Configuration(access_token=channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    print("#" * 40)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    print("#" * 40)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        print("使用者傳入文字訊息")
        print(event)
        line_bot_api = MessagingApi(api_client)
        user_msg = event.message.text
        bot_msg = TextMessage(text=f"您剛剛傳入的文字訊息是: {user_msg}")

        if user_msg in faq:
            bot_msg = faq[user_msg]
        elif user_msg.lower() in ["選單", "menu", "home", "主選單"]:
            bot_msg = menu
            print(bot_msg)
        elif user_msg in ["溫泉", "河濱公園", "老街", "博物館", "教育館", "美術館", "商圈", "市場", "夜市"]:
            text = ""
            res = get_taipeispot_table(user_msg)
            total = len(res)
            print(total)
            if (total > 0):
                for x in range(0,total):
                    name = res[x]['name']
                    tel = res[x]['tel']
                    address = res[x]['address']
                    text += f"景點名稱:{name}" + "\n" + f"電話:{tel}" + "\n" + f"地址:{address}" + "\n"
                    text += f"======================" + "\n"
                    print(name)

            bot_msg = TextMessage(text=text)
            
            


        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    bot_msg
                ]
            )
        )

@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        sticker_id = event.message.sticker_id
        package_id = event.message.package_id
        keywords = ", ".join(event.message.keywords)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    StickerMessage(package_id="11537", sticker_id="52002738"),
                    TextMessage(text=f"您剛剛傳送了一則貼圖. 這是貼圖相關資訊:"),
                    TextMessage(text=f"貼圖包ID 是 {package_id}, 貼圖ID 是 {sticker_id}."),
                    TextMessage(text=f"關鍵字是 {keywords}."),
                ]
            )
        )

@handler.add(MessageEvent, message=LocationMessageContent)
def handle_location_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        latitude = event.message.latitude
        longitude = event.message.longitude
        address = event.message.address
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=f"您剛剛傳送了位置資訊."),
                    TextMessage(text=f"您所在位置的緯度是 {latitude}."),
                    TextMessage(text=f"您所在位置的經度是 {longitude}."),
                    TextMessage(text=f"地址是 {address}."),
                    LocationMessage(title="這是您剛剛傳送的位置資訊.", address=address, latitude=latitude, longitude=longitude)
                ]
            )
        )


# 如果應用程式被執行執行
if __name__ == "__main__":
    print("[伺服器應用程式開始運行]")
    # 取得遠端環境使用的連接端口，若是在本機端測試則預設開啟於port=5001
    port = int(os.environ.get('PORT', 5001))
    print(f"[Flask即將運行於連接端口:{port}]")
    print(f"若在本地測試請輸入指令開啟測試通道: ./ngrok http {port} ")
    # 啟動應用程式
    # 本機測試使用127.0.0.1, debug=True
    # Heroku部署使用 0.0.0.0
    app.run(host="0.0.0.0", port=port)
