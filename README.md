# NKTO
Nankai Trade Online

## Quick Start

先对Vue进行加载:
```shell
cd website/frontend
npm install
npm install iview-theme -g
cd src/mytheme
iview-theme build -o dist/
cd ..
cd ..
npm run build
```
再开启Django测试服务器
```shell
cd website
python manage.py runserver
```