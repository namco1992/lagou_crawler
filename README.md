# lagou_crawler 拉勾网职位信息爬虫
### 1. 概述
利用 scrapy 框架对拉勾网上的职位进行抓取，数据存储至 mongodb 中，后续进行进一步分析导出 json 格式数据，利用 fabric + 定时任务上传更新数据至服务器，完成自动部署。

*由于 scrapy 目前对 py3 尚未完全支持，因此该项目仅在 py2.7下运行测试通过。 *

数据展示网站示例：[http://107.170.207.236/job_analysis/](http://107.170.207.236/job_analysis/)

数据展示项目地址：[https://github.com/namco1992/job_analysis](https://github.com/namco1992/job_analysis)

### 2. 模块
1. 爬虫模块
2. 数据分析，导出为 json 格式数据。
3. 自动部署

### 3. 使用方法
首先参照`settings.py.example`设置 settings.py。

1. 爬虫
```shell
scrapy crawl lagou
```
2. 数据分析
```shell
python analysis/analyze.py
```

3. 自动部署
```shell
fab automatic_deploy
```

### 4. Powered by
- scrapy
- mongodb
- fabric

### 5. LICENCE
MIT
