# ZDSwap
面向中山大学的二手交易小程序：校园转转

## 成员

- 俞沣城
- 宋文慧
- 林佳盈
- 彭宇璇
- 李悦

## 项目链接

- index-site: [index.html](http://47.120.41.234:8080/index.html)
- home-site: [home.html](http://47.120.41.234:8080/home.html)
- login-site: [intro.html](http://47.120.41.234:8080/intro.html)

## how to run with docker

克隆仓库：
```bash
https://github.com/ffengc/ZDSwap.git
cd ZDSwap
```

使用dockerfile进行部署：

**1. 创建dockerfile文件**

```dockerfile
FROM nginx:latest
COPY ./wwwroot /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
```

**2. 给文件添加权限**

创建脚本`ChMod.sh`

```bash
#!/bin/bash
# write by Yufc
# 检查是否提供了目录作为参数
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
# 获取目录参数
directory=$1
# 检查目录是否存在
if [ ! -d "$directory" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi
# 为目录及其子目录下的所有文件和文件夹增加读权限
find "$directory" -type d -exec chmod a+rwx {} \;
find "$directory" -type f -exec chmod a+rwx {} \;
echo "ALL permissions have been added to all files and directories within $directory."
```

运行脚本 `./ChMod.sh ./*`

**3. 部署服务**

```bash
docker build -t nginx-homepage .
docker run -d -p 8080:80 nginx-homepage
```

**部署后访问服务器8080端口即可。**