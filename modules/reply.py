from linebot.v3.messaging import (
    StickerMessage,
    ImageMessage,
    TextMessage,
    LocationMessage,
    TemplateMessage,
    CarouselTemplate,
    CarouselColumn,
    QuickReply,
    QuickReplyItem,
    MessageAction,
    URIAction,
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

faq = {
    '貼圖': StickerMessage(
        package_id='1',
        sticker_id='1'
    ),
    '捷運路網圖': ImageMessage(
        original_content_url="https://web.metro.taipei/pages/assets/images/routemap2023n.png",
        preview_image_url="https://web.metro.taipei/pages/assets/images/routemap2023n.png"
    ),
    '交通': TextMessage(text='請問您想使用何種方式前往？',
                          quick_reply=QuickReply(items=[
                              QuickReplyItem(action=MessageAction(
                                  label="搭乘捷運", text="捷運")
                              ),
                              QuickReplyItem(action=MessageAction(
                                  label="搭乘公車", text="公車")
                              )
                          ])
                          ),
    '捷運': TextMessage(
        text="搭乘捷運至文湖線松山機場站，從3號出口出去後步行約7分鐘即可抵達。"
    ),
    '公車': TextMessage(
        text="搭乘公車至富錦街口站，途經敦化北路，步行約5分鐘即可抵達。"
    ),
    '營業地址': LocationMessage(
        title='觀光局旅遊服務中心(松山機場)',
        address='105台北市松山區敦化北路240號',
        latitude=25.060088,
        longitude=121.5493711
    ),
    '服務時間': TextMessage(
        text='週一至週五 08：00-17：00',
    ),
    '查詢臺北景點': TemplateMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Taipei_Daan_Park_Ecological_Pool.jpg/1920px-Taipei_Daan_Park_Ecological_Pool.jpg",
                    title='景點選單一',
                    text='點選下方按鈕查詢臺北景點',
                    actions=[
                        MessageAction(
                            label='查詢河濱公園',
                            text='河濱公園'
                        ),
                        MessageAction(
                            label='查詢溫泉',
                            text='溫泉'
                        ),
                        MessageAction(
                            label='查詢老街',
                            text='老街'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Taipei_Fine_Arts_Museum_and_China_Eastern_aircraft_20120628.jpg/1280px-Taipei_Fine_Arts_Museum_and_China_Eastern_aircraft_20120628.jpg",
                    title='景點選單二',
                    text='點選下方按鈕查詢臺北景點',
                    actions=[
                        MessageAction(
                            label='查詢博物館',
                            text='博物館'
                        ),
                        MessageAction(
                            label='查詢教育館',
                            text='教育館'
                        ),
                        MessageAction(
                            label='查詢美術館',
                            text='美術館'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://imgcdn.cna.com.tw/www/WebPhotos/1024/20230519/1024x768_wmkn_0_C20230519000132.jpg",
                    title='景點選單三',
                    text='點選下方按鈕查詢臺北景點',
                    actions=[
                        MessageAction(
                            label='查詢商圈',
                            text='商圈'
                        ),
                        MessageAction(
                            label='查詢市場',
                            text='市場'
                        ),
                        MessageAction(
                            label='查詢夜市',
                            text='夜市'
                        )
                    ]
                )
            ]
        )
    )
}

# 主選單
# Carousel Template
# https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template
menu = TemplateMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url="https://www.travel.taipei/image/213208/480x360",
                title='主選單一',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='交通資訊',
                        text='交通'
                    ),
                    MessageAction(
                        label='服務時間',
                        text='服務時間'
                    ),
                    MessageAction(
                        label='營業地址',
                        text='營業地址'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url="https://blog.tripbaa.com/wp-content/uploads/2020/10/plan_2020090317510925776_b.jpg",
                title='主選單二',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='查詢臺北景點',
                        text='查詢臺北景點'
                    ),
                    MessageAction(
                        label='捷運路網圖',
                        text='捷運路網圖'
                    ),
                    URIAction(
                        label='台北捷運官方網站',
                        uri='https://www.metro.taipei/Default.aspx'
                    )
                ]
            )
        ]
    )
)
