# 导包
import requests
import unittest
# 设计用来
class TestClsQueryALL(unittest.TestCase):
    def test_clsQuery_all(self):
        url=r'http://127.0.0.1:8000/api/departments'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)

    def test_clsQuery_2(self):
        url=r'http://127.0.0.1:8000/api/departments'
        param = {"cls_id":"2018T7"}
        res=requests.get(url,param)
        self.assertEqual(200,res.status_code)

    def test_clsQuery_3(self):
        url=r'http://127.0.0.1:8000/api/departments'
        param = {"blur":"1","cls_id": "(.*)2018(.*)","cls_name": "2018?Test??8?"}
        res=requests.get(url,param)
        self.assertEqual(200,res.status_code)

    def test_clsQuery_4(self):
        url=r'http://127.0.0.1:8000/api/departments'
        param = {"blur":"1","cls_id": "(.*)2018(.*)"}
        res=requests.get(url,param)
        self.assertEqual(200,res.status_code)

    def test_clsQuery_5(self):
        url=r'http://127.0.0.1:8000/api/departments'
        param = {"cls_id":["2018T7","2018T5"]}
        res=requests.get(url,param)
        self.assertEqual(200,res.status_code)

    def test_clsQuery_6(self):
        url=r'http://127.0.0.1:8000/api/departments'
        param = {"cls_id":["2018T7","2018T5"],"cls_name":["2018?Test??9?","2018?Test??8?"]}
        res=requests.get(url,param)
        self.assertEqual(200,res.status_code)

if __name__ == '__main__':
    unittest.main()