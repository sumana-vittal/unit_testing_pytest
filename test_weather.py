from numpy.ma.testutils import assert_equal

from weather import get_weather

def test_get_weather():
    data = get_weather(26)
    assert_equal(data,'hot')