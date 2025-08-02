from analysis import gc_content

def test_gc_content():
    assert gc_content("GCGC") == 1.0
    assert gc_content("ATAT") == 0.0
