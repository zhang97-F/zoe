# 导包
import requests
import unittest
# 设计用来
class TestDepPost(unittest.TestCase):

    def test_depPost_all(self):
        url = r'http://localhost:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data": [{"dep_id":"T17","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201,res.status_code)
    def test_depPost_2required(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "hhh0"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201,res.status_code)

    def test_depPost_3(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type":"application/json"}
        req_data = r'{"data":[{"dep_id": "","dep_name":"333","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201,res.status_code)

    def test_depPost_4(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type":"application/json"}
        req_data = r'{"data":[{"dep_id": "a4","dep_name":"","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201,res.status_code)

    def test_depPost_5(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a5","dep_name":"123456","master_name":"false","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201, res.status_code)

    def test_depPost_6(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a6","dep_name":"123456","master_name":"","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test_depPost_7(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a7","dep_name":"123456","master_name":"嘿嘿院长","slogan":""}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test_depPost_8(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a8","dep_name":"hehe","master_name":"嘿嘿院长","slogan":"32.99"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test_depPost_9(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a9","dep_name":"123.456","master_name":"FALSE","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201, res.status_code)

    def test_depPost_10(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "true","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test_depPost_11(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a11","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test_depPost_12(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a12","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test_depPost_13(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a12","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        resJson=res.json()
        temp = resJson.get('create_success').get("count")
        self.assertEqual(temp, 1)

    def test_depPost_14(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a14","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        resJson=res.json()
        temp = resJson.get('create_success').get("count")
        self.assertEqual(temp, 1)

    def test_depPost_15(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        req_head = {"Content-Type": "application/json"}
        req_data = r'{"data":[{"dep_id": "a15","dep_name":"123456","master_name":"嘿嘿院长","slogan":"hhhhjjj"}"}]}'
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        resJson=res.json()
        temp = resJson.get('create_success').get("count")
        self.assertEqual(temp, 1)

if __name__ == '__main__':
    unittest.main()




