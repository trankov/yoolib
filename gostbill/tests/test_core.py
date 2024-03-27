from .. import (
    core,
    core_models as cm,
)


def test_service_data_enums_exists():
    assert cm.ServiceData.Charset
    assert cm.ServiceData.FormatID
    assert cm.ServiceData.FormatVersion


def test_service_data_instantiation():
    expected_service_data_str = 'ST00012'
    service_data = cm.ServiceData()

    assert service_data
    assert service_data.format_id == cm.ServiceData.FormatID.ST
    assert service_data.format_version == cm.ServiceData.FormatVersion.DEFAULT
    assert service_data.encoding == cm.ServiceData.Charset.UTF8
    assert str(service_data) == expected_service_data_str
