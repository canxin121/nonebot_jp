import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.typing import T_State

def send_request(text):
    url = 'https://www.jiuwa.net/tools/jupai/index.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/16.2 Mobile/15E148 Safari/604.1',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '14',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'wx=show',
        'Host': 'www.jiuwa.net',
        'Origin': 'https://www.jiuwa.net',
        'Referer': 'https://www.jiuwa.net/jupai/',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        "t": text
    }

    response = requests.post(url, headers=headers, data=data)

    return "https://www.jiuwa.net" + response.text


print(send_request("早安"))

jp = on_command("jp")

@jp.handle()

async def jpmk(bot: Bot, event: Event, state: T_State):
    getmsg = event.get_message()
    text = getmsg[0].data['text'][4:]
    url = send_request(text)
    img = MessageSegment.image(url)

    await jp.finish(img)

