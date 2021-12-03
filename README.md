# 🐳新版我在校园打卡程序Docker版

## 👋介绍

本项目让你可以轻松实现我在校园小程序自动"晨晚检"和"健康打卡"，让你不用再为此烦恼，把更多时间花在更有意义的事情上

本仓库是[zimin9/WoZaiXiaoYuanPuncher](https://github.com/zimin9/WoZaiXiaoYuanPuncher)的Docker版本

感谢[zimin9](https://github.com/zimin9)为我们带来的便利

本项目是因为看到原作者由做docker版的计划，在使用过程中也觉得使用docker来部署运行应该会相对方便一点，所以基于原作者的仓库开发了此版本，最主要的打卡接口请求代码还是原作者的。

在使用过程中还发现原小程序对账号密码使用的限制，即你重置密码后只能用账密登录一次，之后再次登录就一直显示密码错误，错误5次账号还会被冻结24小时，所以最后感觉还是抓包拿到jwsession最稳。

按照[使用方法](#🔥使用方法)开始试试吧，如果对你有帮助不妨点个小小的`Star`✨

## 🔥使用方法

### 💻环境准备

* Docker
* python3

### 🚀快速开始

**拉取源码**

在你安装了Docker的服务器或电脑本地克隆本项目，或者下载后上传

```shell
git clone https://github.com/ccqstark/WoZaiXiaoYuanPuncher-Docker.git
```

**配置信息**

cd进项目目录后，修改配置文件

```shell
vim source.json
```

主要对`usernanme`，`password`， `notify_token`进行设置，地址的按我给的就行

```json
[
  {
    "username": "一般是手机号",
    "password": "忘记密码的话可以在小程序端重置密码，但是还是建议抓包拿jwsession",
    "temperature": "36.5",
    "latitude": "23.065038",
    "longitude": "113.399206",
    "country": "中国",
    "city": "广州市",
    "district": "番禺区",
    "province": "广东省",
    "township": "小谷围街道",
    "street": "大学城外环东路178",
    "myArea": "",
    "areacode": "",
    "userId": "",
    "notification_type": "PushPlus",
    "notify_token": "关注公众号PushPlus即可获得个人token"
  }
]
```

接着就对小程序进行抓包，拿到`jwsession`

（不太清楚如何抓包的请看下面的[抓包教程](#📦抓包教程)）

**设置jwsession**

之后运行`init.py`设置jwsession（要安装python3环境）

```shell
python3 init.py
```

根据提示进行输入设置`username`和`jwsession`

**构建镜像**

```shell
docker build -t puncher .
```

**运行容器**

```shell
docker run -d --name="puncher" puncher
```

第一次运行容器后会尝试一次打卡，如果你设置了PushPlus就会接受到一条消息，以此测试容器是否正常运行起来了

如果是用自己电脑要确保打卡时间容器是运行着的噢

### ✅更新jwsession

由于jwsession的有效期未知，所以在过期时可以通过以下方式进行更新（应该还是够用很久的，过期了再抓个包也不难）

进入容器

```shell
docker exec -it puncher /bin/bash
```

运行`init.py`

```shell
python3 init.py
```

根据提示再次输入username和jwsession就会提示更新成功

之后使用`ctrl`+`P`+`Q`退出容器，容器才能继续正常运行

## 📦抓包教程

### iOS

iOS推荐这款`Stream`应用，简洁好用，在app store中即可安装

按照提示安装信任证书后，开始抓包，并通过域名筛选出`gw.wozaixiaoyuan.com`的请求，在请求头部的Cookie中找到`JWSESSION`字段，复制其值即可

![](https://cdn.jsdelivr.net/gh/ccqstark/image-bed/images/20210926214912.png)

### 安卓

安卓的话这类软件应该更多，用法也差不多，大家去软件商店搜索即可

## 🔗其它版本友链

* 云函数版：[Chorer/WoZaiXiaoYuanPuncher-cloudFunction](https://github.com/Chorer/WoZaiXiaoYuanPuncher-cloudFunction)
* GitHub Actions版：[jimlee2002/WoZaiXiaoYuanPuncher-Actions](https://github.com/jimlee2002/WoZaiXiaoYuanPuncher-Actions)

## ⚠️声明

1. 本项目仅供编程学习/个人使用，请遵守Apache-2.0 License开源项目授权协议。
2. 请在国家法律法规和校方相关原则下使用。
3. 开发者不对任何下载者和使用者的任何行为负责。
4. 本程序无任何后门，所有数据仅存留于使用者机器上。
5. 请不要轻易将自己的账号信息告诉他人。

