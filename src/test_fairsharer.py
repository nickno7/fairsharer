from fairsharer import fair_sharer

def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    assert fair_sharer([1000, 200, 600, 900],2) == [900, 300, 700, 800]
