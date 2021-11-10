import pytest
import temp

def test_temperature():
  assert type(temp.get_temperature()) == int
  assert temp.temp > 50
  
def test_humidity():
  assert type(temp.get_humidity()) == int
  assert temp.humidity > 100
  
