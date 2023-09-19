from main import Rectangle

def test_rectangle_area():
    rect = Rectangle(3, 4)
    assert rect.get_area() == 12

def test_rectangle_area2():
    rect = Rectangle(2, 5)
    assert rect.get_area() == 10

def test_negative_rectangle_area():
    rect = Rectangle(-3, 4)
    assert rect.get_area() == -12