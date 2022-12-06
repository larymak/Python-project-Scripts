import time

startTime_1 = time.time()
import pandas as pd
import numpy as np
executionTime_1 = (time.time() - startTime_1)
print('Time to import modules: ' + str(executionTime_1))

startTime_2 = time.time()
df = pd.DataFrame(np.random.randint(1,9999,size=(10000000, 1)), columns=['Random numbers'])
df['Random numbers'] = df['Random numbers'].astype(str)
executionTime_2 = (time.time() - startTime_2)
print('Time to run the main Python script: ' + str(executionTime_2))
