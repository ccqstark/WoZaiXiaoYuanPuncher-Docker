FROM python:3.7

MAINTAINER ccqstark<ccqstark@qq.com>

COPY . /app/

WORKDIR /app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests schedule

RUN echo "Asia/Shanghai" > /etc/timezone

CMD ["python", "main.py"]
