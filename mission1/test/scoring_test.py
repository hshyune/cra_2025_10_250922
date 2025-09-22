import pytest
import os
import sys
parent_folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_folder_path)
from attendance import input2

@pytest.mark.parametrize("name, attendance_weekday, expected_output",[
    ("Umar","monday",1),
    ("Daisy","tuesday",1),
    ("Alice","tuesday",1),
    ("Xena","saturday",2),
    ("Ian","tuesday",1),
    ("Hannah","monday",1),
    ("Hannah","thursday",1),
    ("Ethan","wednesday",3),
    ("Xena","wednesday",3),
    ("Daisy","tuesday",1),
])
def test_scoring(name, attendance_weekday, expected_output):
    assert input2(name, attendance_weekday) == expected_output
