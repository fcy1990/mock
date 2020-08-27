

import pytest
from common import mock_data

class TestMock():

    def test_payment_type(self,mocker):
        pay=mock_data.PaymentType()
        pay.payapi=mocker.patch('common.mock_data.PaymentType.payapi',return_value={'SCORE': 1})
        status = pay.paymenttype()
        print('======')
        print(status)
        assert status == '支付分'
        print('成功')

if __name__ == '__main__':
    command = '-q test_mock_data.py::TestMock::test_payment_type'
    pytest.main(command)

