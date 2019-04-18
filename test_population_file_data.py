#contents of test_population_file_data.py
import pandas as pd

def test_input():
	a = pd.read_csv("input.txt",index_col=0)
	assert int(float(a['2010']['World'])) == 6853