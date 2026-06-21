import pandas as pd
from torch.utils.data import Dataset

data = {'text': ['Hello world', 'How are you?', 'Goodbye!'],
        'label': [0, 1, 0] }
df = pd.DataFrame(data)

 