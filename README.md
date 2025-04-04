

```
# 设置环境变量（Windows）
set FLASK_APP=app
set FLASK_ENV=development

# 初始化数据库
flask db init
flask db migrate -m "Fix relationship conflicts"
flask db upgrade

# 启动服务器
flask run

npm install
npm run build
npm run watch

# 安装TailwindCSS
npm init -y

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm cache clean --force
npm cache verify
npm install -D tailwindcss@3.4.17

tree /f > directory.txt

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


gunicorn --config deploy/gunicorn.conf.py "app:create_app()"

cd hexo-sitenpm 
install hexo-theme-next

{
  "name": "hexo-site",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "build": "hexo generate",
    "clean": "hexo clean",
    "deploy": "hexo deploy",
    "server": "hexo server"
  },
  "hexo": {
    "version": "7.3.0"
  },
  "dependencies": {
    "hexo": "^7.3.0",
    "hexo-generator-archive": "^2.0.0",
    "hexo-generator-category": "^2.0.0",
    "hexo-generator-feed": "^3.0.0",
    "hexo-generator-index": "^4.0.0",
    "hexo-generator-tag": "^2.0.0",
    "hexo-renderer-ejs": "^2.0.0",
    "hexo-renderer-marked": "^7.0.1",
    "hexo-renderer-stylus": "^3.0.1",
    "hexo-server": "^3.0.0",
    "hexo-theme-next": "^8.23.0"
  }
}



npm install hexo-theme-next@latest
npm install hexo-generator-feed --save



plugins: hexo-generate-feed

# Feed Plugin
feed:
  type: atom
  path: atom.xml
  limit: 0
  hub:
  content: true
  content_limit: 140
  content_limit_delim: ' '
  order_by: -date
  

```



