# 📲 新版我在校园打卡程序Docker版🐳



## 使用方法

在你安装了Docker的本地或者服务器上克隆本项目，或者下载后上传

```shell
git clone https://github.com/ccqstark/WoZaiXiaoYuanPuncher-Docker.git
```

cd目录后，修改配置文件

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

接着就对小程序进行抓包，拿到jwsession

运行`init.py`设置jwsession（要安装python3环境）

```shell
python3 init.py
```

根据提示进行输入设置`username`和`jwsession`



构建镜像

```shell
docker build -t puncher .
```

运行容器

```shell
docker run -d --name="puncher" puncher
```



## 更新jwsession

进入容器

```shell
docker exec -it puncher /bin/bash
```

