# nosetests --nocapture  tests/test_fit_file_header.py

from fit_tool.fit_file_header import ProtocolVersion, ProfileVersion, FitFileHeader

def test_protocol_version():
    protocol_version = ProtocolVersion(2, 3)
    assert str(protocol_version) == '2.3'
    bytes1 = protocol_version.to_bytes()
    pv2 = ProtocolVersion.from_bytes(bytes1)
    bytes2 = pv2.to_bytes()
    assert bytes1 == bytes2

def test_profile_version():
    profile_version = ProfileVersion(21, 60)
    assert str(profile_version) == '21.60'
    bytes1 = profile_version.to_bytes()
    pv2 = ProfileVersion.from_bytes(bytes1)
    bytes2 = pv2.to_bytes()
    assert bytes1 == bytes2

def test_generate_crc():
    protocol_version = ProtocolVersion(2, 3)
    profile_version = ProfileVersion(21, 60)
    FitFileHeader.generate_crc(protocol_version, profile_version, 6552343)

def test_conversion_without_crc():
    header1 = FitFileHeader(protocol_version=ProtocolVersion(2, 3), profile_version=ProfileVersion(21, 60),
                           records_size=4294967295)
    bytes1 = header1.to_bytes()
    assert len(bytes1) == 12
    header2 = FitFileHeader.from_bytes(bytes1)
    bytes2 = header2.to_bytes()
    assert bytes1 == bytes2

def test_conversion_with_crc():
    header1 = FitFileHeader(protocol_version=ProtocolVersion(2, 3), profile_version=ProfileVersion(21, 60),
                           records_size=4294967295, crc=500)
    bytes1 = header1.to_bytes()
    assert len(bytes1) == 14
    header2 = FitFileHeader.from_bytes(bytes1)
    bytes2 = header2.to_bytes()
    assert bytes1 == bytes2
