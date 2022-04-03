import requests
import execjs

class baiDuFanYi:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
        }
        self.s = requests.session()
        self.getCookieToken()
        html = self.getCookieToken()
        self.token = html.split("token: '")[1].split("'")[0]
        with open('./baidu.js', encoding='utf-8') as f:
            self.jiaomi = execjs.compile(f.read())



    def getCookieToken(self):
        url = "https://fanyi.baidu.com/translate?aldtype=16047&query=%E9%99%88%E4%B8%8D%E4%B8%8D%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh"
        req = self.s.get(url,headers=self.headers)
        return req.text

    def getFanYi(self, data,sign):
        url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
        table = {
            'domain':"common",
            'from':"zh",
            'query':data,
            'sign':sign,
            'simple_means_flag':'3',
            'to':"en",
            'token':self.token
        }
        req = self.s.post(url,data=table)
        return req.json()

    def getFanYimain(self, data):
        sign = self.jiaomi.call('e', data)
        print(sign)
        return self.getFanYi(data, sign)



if __name__ == '__main__':
    # 初始化
    cbb = baiDuFanYi()

    # 开始翻译
    data = "陈不不"
    k = cbb.getFanYimain(data)
    print(k)

    # 开始翻译
    data = "我的世界"
    k = cbb.getFanYimain(data)
    print(k)

