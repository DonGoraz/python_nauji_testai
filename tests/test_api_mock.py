from unittest.mock import patch, MagicMock
from newcalc.api_mock import API, get_only_numbers


def test_api_read_only_numbers():
    test_data = ["1,2,3,4,5,6,7,8,9,10,lip,qwqwq,qwew,zx,ds,dsg,gf", "515,154,58f,fff,166"]
    expected = "1|2|3|4|5|6|7|8|9|10|515|154|166"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('newcalc.api_mock.API', fake_api):
        result = get_only_numbers()
        assert result == expected
