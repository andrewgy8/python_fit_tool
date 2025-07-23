from fit_tool.utils.crc import crc16

def test_crc16():
    data = '123456789'.encode('utf-8')
    result = crc16(data)
    assert result == 0xBB3D
