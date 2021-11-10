import pytest
import temp

def test_temperature():
  assert type(temp.temp) == int
  assert temp.temp > 50
  
def test_humidity():
  assert type(temp.humidity) == int
  assert temp.humidity > 100
  
