import traceback
try:
    import matplotlib
    print('matplotlib.__file__:', matplotlib.__file__)
    import matplotlib.pyplot as plt
    print('pyplot OK')
except Exception:
    traceback.print_exc()
