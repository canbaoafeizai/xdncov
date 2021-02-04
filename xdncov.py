#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, time, logging, requests

g_session = requests.session()
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
  datefmt='%a, %d %b %Y %H:%M:%S',
  handlers=[logging.StreamHandler(), logging.FileHandler(f"output.log", "a")]
)

def login():
  data = { "username": os.environ["username"], "password": os.environ["password"] }
  headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36" }
  logging.info(g_session.post(url="https://xxcapp.xidian.edu.cn/uc/wap/login/check", data=data, headers=headers).text)

def submit():
  data = {
    "tw": 4,
    "province": os.environ["province"],
    "city": os.environ["city"],
    "district": os.environ["district"],
    "zgfxdq": 0, "mjry": 0, "csmjry": 0, "sfcxtz": 0 , "sfjcbh": 0, "sfcxzysx": 0, "sfyyjc": 0 , "jcjgqr": 0, "sfzx": 0, "sfjcwhry": 0, "sfjchbry": 0, "sfcyglq": 0, "sftjhb": 0, "sftjwh": 0, "sfjcjwry": 0, "szsqsfybl": 0, "sfsqhzjkk": 0, "sfygtjzzfj": 0, "ismoved": 0
  }
  data["area"] = " ".join((os.environ["province"], os.environ["city"], os.environ["district"])); data["address"] = data["area"].replace(" ", "")
  headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36" }
  r = g_session.post(url="https://xxcapp.xidian.edu.cn/ncov/wap/default/save", data=data, headers=headers)
  logging.info(r.text)
  if "key" in os.environ:
    data = { "text": f'{time.strftime("%Y-%m-%d", time.localtime())} {r.json()["m"]}', "desp": r.text }
    requests.post(url=f'https://sc.ftqq.com/{os.environ["key"]}.send', data=data)

def main(): login(); submit()

if __name__ == "__main__": main()
