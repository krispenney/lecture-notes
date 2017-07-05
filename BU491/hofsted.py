#%   matplotlib inline

# Data from - http://www.internetlivestats.com/internet-users/tunisia/
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

sns.set(style="whitegrid")
sns.set_palette(sns.color_palette("muted", 10))

df = pd.DataFrame({ "Canada": {
        "Power Distance": 39,
            "Individualism": 80,
                "Masculinity": 52,
                    "Uncertainty Avoidance": 48,
                        "Pragmatism": 36
                        }})

df2 = pd.DataFrame({ "India": {
        "Power Distance": 77,
            "Individualism": 43,
                "Masculinity": 56,
                    "Uncertainty Avoidance": 40,
                        "Pragmatism": 51
                        }})

df = pd.concat([df, df2], axis=1)
df.reset_index()
df.plot.bar()
plt.show()
