import json
import boto3
import urllib
import re
import os

def getUser(token, userId):
    print('トークン: ', token)
    print('ユーザーID: ', userId)
    url = 'https://api.line.me/v2/bot/profile/'+str(userId)
    headers = {
        'Authorization': token
    }
    userInfo = ''
    request = urllib.request.Request(url, method='GET', headers=headers)
    with urllib.request.urlopen(request) as res:
        userInfo =res.read().decode()
        userInfo = json.loads(userInfo)
        print('デコードしたよー: ', type(userInfo))
    return userInfo['displayName']

def lambda_handler(event, context):
    print ('DEBUG: ', event)
    # Userid U79ed33e5015fae2175750ad82911b597
    url = "https://api.line.me/v2/bot/message/reply"
    method = "POST"
    headers = {
        'Authorization': 'Bearer vohMaKjQ2W5DbGo0JQT8wNH3LmJmZ35voupSVVDg0zvr77W2WjWC2auq3zu1UmzFmMCwBRywWpWOlOMw2OvQuf/zTk2O9r0VSXobMiwcC+L18hv8cA2JtZybckJi7xYQ120qO6SN1+D8yW7AWJtJbwdB04t89/1O/w1cDnyilFU=',
        'Content-Type': 'application/json'
    }

    if (event['events'][0]['type'] == "postback"):
        print('ポストバック後')
        if (event['events'][0]['postback']['data'] == "blog"):
            message = [
                {
                    "type": "text",
                    "text": "ブログをお探しします！",
                    "quickReply": {
                        "items": [
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "おすすめ",
                                    "data": "Recommended",
                                    "displayText": "おすすめ"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "キーワード検索",
                                    "data": "keyword",
                                    "displayText": "キーワード検索"
                                }
                            }
                        ]
                    }
                }
            ]
        elif (event['events'][0]['postback']['data'] == "Recommended"):
            message = [
                {
                    "type": "text",
                    "text": "おすすめはこちら！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/blog/news/"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "service"):
            message = [
                {
                    "type": "text",
                    "text": "どのようなサービスをお探しでしょうか？",
                    "quickReply": {
                        "items": [
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "AWS導入",
                                    "data": "AWS",
                                    "displayText": "AWS"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "Backup",
                                    "data": "Backup",
                                    "displayText": "Backup"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "AWS移行",
                                    "data": "Migration",
                                    "displayText": "Migration"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "アプリ開発",
                                    "data": "app",
                                    "displayText": "app"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "監視・運用",
                                    "data": "operation",
                                    "displayText": "operation"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "VPN・専用線",
                                    "data": "VPN",
                                    "displayText": "VPN"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "鳴子",
                                    "data": "NARUKO",
                                    "displayText": "NARUKO"
                                }
                            }
                        ]
                    }
                }
            ]
        elif (event['events'][0]['postback']['data'] == "AWS"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#aws_consul"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "Backup"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#cloud"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "Migration"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#cloudmigration"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "app"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#application"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "operation"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#network"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "VPN"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/service/#monitoring"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "NARUKO"):
            message = [
                {
                    "type": "text",
                    "text": "サービスサイトにご案内します！"
                },
                {
                    "type": "text",
                    "text": "https://xp-cloud.jp/naruko/"
                }
            ]
        elif (event['events'][0]['postback']['data'] == "keyword"):
            message = [
                {
                    "type": "text",
                    "text": "「検索」の後にスペースを入れてキーワードを入力してください。\n\n例）検索 DynamoDB\n\nキーワードにスペースが含まれる場合にはAND検索となります。"
                }
            ]
    elif (event['events'][0]['type'] == "message"):
        if (event['events'][0]['message']['text'] == "案内"):
            message = [
                {
                    "type": "text",
                    "text": "こんにちは！ご用件をお伺いできますでしょうか？",
                    "quickReply": {
                        "items": [
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "blog",
                                    "data": "blog",
                                    "displayText": "blog"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "service",
                                    "data": "service",
                                    "displayText": "service"
                                }
                            }
                        ]
                    }
                }
            ]
        elif('ブロードキャスト' in event['events'][0]['message']['text']):
            userInfo = getUser('Bearer vohMaKjQ2W5DbGo0JQT8wNH3LmJmZ35voupSVVDg0zvr77W2WjWC2auq3zu1UmzFmMCwBRywWpWOlOMw2OvQuf/zTk2O9r0VSXobMiwcC+L18hv8cA2JtZybckJi7xYQ120qO6SN1+D8yW7AWJtJbwdB04t89/1O/w1cDnyilFU=', event['events'][0]['source']['userId'])
            url_broadcast = 'https://api.line.me/v2/bot/message/broadcast'
            messages=[
                {
                    "type":"text",
                    "text":"ブロードキャストで送るぞい!!"
                },
                {
                    "type":"text",
                    "text": "{userInfo}さんが送りました".format(userInfo=userInfo)
                }
            ]
            params = {
                "replyToken": event['events'][0]['replyToken'],
                "messages": messages
            }
            request = urllib.request.Request(url_broadcast, json.dumps(params).encode("utf8"), method='POST', headers=headers)
            with urllib.request.urlopen(request) as res:
                body = res.read()

        elif("映画" in event['events'][0]['message']['text']):
            message = [
                # thumbnailImageUrlにて有効なURLをお設定しないと動かいないよ!!
                    # {
                    #     "type": "template",
                    #     "altText": "this is a buttons template",
                    #     "template": {
                    #         "type": "buttons",
                    #         "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
                    #         "title": "好きな映画",
                    #         "text": "どれか選んでね",
                    #         "actions": [
                    #             {
                    #                 "type": "message",
                    #                 "label": "シャークネード3",
                    #                 "text": "シャークネード3"
                    #             },
                    #             {
                    #                 "type": "message",
                    #                 "label": "ジョーズ",
                    #                 "text": "ジョーズ"
                    #             }
                    #         ]
                    #     }
                    # }
                    {
                        "type": "text",
                        "text": "どのようなサービスをお探しでしょうか？",
                        "quickReply": {
                            "items": [
                                {
                                "type": "action",
                                "action": {
                                    "type": "cameraRoll",
                                    "label": "Send photo"
                                }
                                },
                                {
                                "type": "action",
                                "action": {
                                    "type": "camera",
                                    "label": "Open camera"
                                }
                                },
                                {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label": "AWS導入",
                                    "data": "AWS",
                                    "displayText": "AWS"
                                }
                            }
                            ]
                        }
                    }
                    
                ]
        elif (re.match("検索", event['events'][0]['message']['text'])):
            keywords = event['events'][0]['message']['text'].split()
            if (len(keywords) > 1):
                keywords.remove("検索")
                keyword = "+".join(keywords)
                result = "https://xp-cloud.jp/blog/?s=" + str(keyword)
                message = [
                    {
                        "type": "text",
                        "text": "検索結果をご案内します。"
                    },
                    {
                        "type": "text",
                        "text": result
                    }
                ]
            else:
                message = [
                    {
                        "type": "text",
                        "text": "入力を正しく処理できませんでした。\n「検索」の後にスペースを入れてキーワードを入力してください。\n\n例）検索 DynamoDB"
                    }
                ]
        elif (event['events'][0]['message']['text'] == "こんにちは"):
            message = [
                {
                    "type": "text",
                    "text": "こんにちは！"
                }
            ]
        else:
            message = [
                {
                    "type": "text",
                    "text": "ご利用の際には「案内」と入力してください。"
                }
            ]
    if message is not None:
        params = {
            "replyToken": event['events'][0]['replyToken'],
            "messages": message
        }

        request = urllib.request.Request(url, json.dumps(params).encode("utf8"), method=method, headers=headers)
        with urllib.request.urlopen(request) as res:
            body = res.read()
    return 0