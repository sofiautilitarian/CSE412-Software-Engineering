# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:35:37 2023

@author: Sofia
"""

import pandas as pd
from datasets import load_dataset
dataset = load_dataset("code_x_glue_cc_clone_detection_big_clone_bench")
df = pd.DataFrame(dataset['train'])
df.head(5)