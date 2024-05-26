#!/usr/local/bin/python3
import sys
import json

# custom module
import loglib
from linelib import Reply

SAMPLE_MESSAGE: dict = {'type': 'text', 'text': 'Hello world' }
CHANNEL_ACCESS_TOKEN: str = "gE5Dx8Sr0C1OgA/kz4DFXmZiVgBMycfzhD4H3CCNWwtqEICmWH51lCBBqfQ5NPR9eh16Iud52+ELX1y8bwqEv2V4G+InoGnt065shnkpX5lJS8YtmHde59z/xpJJ3k0wY5TUZNRxnguBO5RHgfx7+gdB04t89/1O/w1cDnyilFU="
logger = loglib.get(__name__)


def main():
    body: dict = json.load(sys.stdin)
    event: dict = body["events"][0]
    rtoken: str = event['replyToken']
    etype: str = event["type"]
    reply = Reply(CHANNEL_ACCESS_TOKEN, rtoken)

    if etype == "message":
        text: str = event["message"]["text"]
        reply.add({'type': 'text', 'text': text })

    reply.send()


if __name__ == "__main__":
    print("Content-Type: text/plain\r\n")
    try:
        main()
    except Exception as e:
        logger.exception(str(e))
