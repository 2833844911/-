# 百度翻译接口逆向

#### [逆向教程](https://www.bilibili.com/video/BV1iY411J7ZA?spm_id_from=333.337.search-card.all.click)



#### 脚本的使用

```python
# 初始化
cbb = baiDuFanYi()

# 开始翻译
data = "陈不不"
k = cbb.getFanYimain(data)
print(k)
```

输出的结果是百度翻译的接口返回信息