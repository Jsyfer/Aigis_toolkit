# Aigis_toolkit

toolkit for web game 千年戦争アイギス

## build docker image

```shell
docker build -t aigis_toolkit_image .
```

## run with docker

```shell
docker run -d \
  --name aigis_toolkit \
  -v /mnt/user/appdata/aigis_toolkit/aigis_toolkit.db:/app/aigis_toolkit.db \
  -p 8100:8000 \
  aigis_toolkit_image
```
