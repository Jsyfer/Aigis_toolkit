# Aigis_toolkit

this is a Unit management for web game 千年戦争アイギス for personal use.

Unit infomation scraped from http://wikiwiki.jp/aigiszuki/

# installation

> prerequest: you need docker environment installed.

1. rename `aigis_toolkit_sample.db` to `aigis_toolkit.db`

2. build docker image

   ```shell
   docker build -t aigis_toolkit_image .
   ```

3. run with docker

   Here is an example (you can change name and port for your needs)

   ```shell
   docker run -d \
     --name aigis_toolkit \
     -v /mnt/user/appdata/aigis_toolkit/aigis_toolkit.db:/app/aigis_toolkit.db \
     -p 8100:8000 \
     aigis_toolkit_image
   ```
