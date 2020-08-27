
import requests
class PaymentType():
    def payapi(self):
        url = 'http://..........'
        headers = '{"Content-Type": "application/json"}'
        request_data = {
        "memberId": "#############",
        "wxOpenid": "#########",
        "sourceCode": "wxapp"
    }
        res = requests.post(url=url,headers=eval(headers),json=request_data)
        result = res.json()
        return result['obj']['paymentTypeV2']   #返回具体的支付方式代码

    def paymenttype(self):
        res = self.payapi()
        if res == {'SCORE': 1}:
            print('-------')
            print('支付分')
            return '支付分'
        elif res == {'SCORE': 0,'online': 1}:
            return '在线支付'
