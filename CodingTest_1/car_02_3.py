import pandas as pd
class Record:
    """
    def __init__(self,file):
        self.file = file
    """


    def make_df(self,file):
        df = pd.read_csv(file)
        dfn = pd.DataFrame(df.values, columns=['時間', '走行距離'])
        return dfn

    def load_calc(self, dfn):
        loads = dfn['走行距離'].sum()
        return loads