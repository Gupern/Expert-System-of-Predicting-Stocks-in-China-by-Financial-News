## nginx的配置
```nginx
        location / {
            root   /<your_esps_path>/src/templates/news/;
            index  index.html index.htm;
        }
        # esps的api转发
        location /esps/ {
            proxy_pass http://localhost:8888/;
        }

```