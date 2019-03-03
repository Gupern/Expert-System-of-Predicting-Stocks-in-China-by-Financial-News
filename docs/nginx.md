## nginx的配置
```nginx
        location / {
            root   /<your_path>/src/engine/templates/news/;
            index  index.html index.htm;
        }
        # esps的api转发
        location /esps/ {
            proxy_pass http://localhost:8888/;
        }

```