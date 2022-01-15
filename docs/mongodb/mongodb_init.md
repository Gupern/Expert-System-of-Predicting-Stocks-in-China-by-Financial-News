## download server
https://www.mongodb.com/try/download/community

## manual
https://mongodb.net.cn/manual/

## download compass -- the GUI client
https://www.mongodb.com/try/download/compass

- use default setting, and connect to server by noauth and localhost:27017

## 常用命令 

### compass模糊搜索中文

`{"industry": {$regex:"地产"}}`


# schema info 
## db
`esps`

## collection 

### stock_basic  股票基本信息

|名称|类型|默认显示|描述|
|-|-|-|-|
|ts_code|str|Y|TS代码|
|symbol|str|Y|股票代码|
|name|str|Y|股票名称|
|area|str|Y|地域|
|industry|str|Y|所属行业|
|fullname|str|N|股票全称|
|enname|str|N|英文全称|
|cnspell|str|N|拼音缩写|
|market|str|Y|市场类型（主板/创业板/科创板/CDR）|
|exchange|str|N|交易所代码|
|curr_type|str|N|交易货币|
|list_status|str|N|上市状态,L上市,D退市,P暂停上市|
|list_date|str|Y|上市日期|
|delist_date|str|N|退市日期|
|is_hs|str|N|是否沪深港通标的,N否,H沪股通,S深股通|