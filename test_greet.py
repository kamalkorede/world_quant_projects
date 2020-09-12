from greet import convert_to_fahr


def test_convert_to_fahr():
    temp_Fs = [-40, 32, 212]
    temp_Cs = [-40, 0, 100]
    
    for temp_F, temp_C in zip(temp_Fs,temp_Cs):
        assert temp_F == convert_to_fahr(temp_C)
