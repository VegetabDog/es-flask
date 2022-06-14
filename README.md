# es-flask
es实现搜索功能，flask将搜索结果通过网页展示。

#### 环境配置

**需要安装es和ik分词器，建议两者版本选择一样。**

编译器的话我用的是pycharm，再者就是包的安装，如果安装失败，换个镜像源就可以（自行百度）。

#### 使用说明

* 先启动es，在es的安装目录双击elasticsearch.bat文件。

* 在我这个项目中需要先运行InputData.py文件，把数据导入es中。数据是通过python爬虫获取并存入数据库（MySQL）中。

* 直接运行app.py文件，在浏览器上输入运行输出的网址即可。

#### 运行结果

![image-20220614142707470](C:\Users\29705\AppData\Roaming\Typora\typora-user-images\image-20220614142707470.png)

#### 不足

没有对搜索结果进行分页，只是简单的展示了搜索结果。

