# pwn-calculate
用 Docker 架設的基礎 pwn 題目
## Requirement
- [Installed Docker](https://docs.docker.com/install/)
- 10001/tcp opened
## Intall
1. 建立 Docker 鏡像
```sh
sudo docker build -t pwn .
```
2. 運行 pwn
```sh
sudo docker run -d  -p 10001:4444 -t pwn
```
3. 檢查有沒有執行成功
```sh
sudo docker ps
```
