import pytest
import temp

def test_temperature():
  assert type(temp) == int
  assert temp > 50
  
def test_humidity():
  assert type(humidity) == int
  assert humidity > 100
  
