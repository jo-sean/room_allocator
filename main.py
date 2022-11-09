# Sean Perez
# Date: 09/11/2022

import numpy as np
import pandas as pd


def main():
    s = pd.DataFrame([1, 3, 5, np.nan, 6, 8], index=list('ABCDEF'), columns=['Test'])
    print(s)


if __name__ == "__main__":
    main()

