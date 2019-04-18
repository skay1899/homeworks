#contents of test_population_file.py
import pandas as pd

def test_input():
	a = pd.read_csv("input.txt",index_col=0)
	assert len(a.index) == 232 and len(a.columns) == 31