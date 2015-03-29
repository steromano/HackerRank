import numpy as np
import fileinput
from sklearn.ensemble import RandomForestClassifier

## Read and parse input -------------------------------------------------------
def parse_record(line, labeled = True):
    rec_id = line[0]
    rec_y = line[1] if labeled else None
    k = 2 if labeled else 1
    rec_x = map(lambda x: x.split(":")[1], line[k:])
    return rec_id, rec_x, rec_y

inputf = fileinput.input()
# Training set
n, m = map(int, inputf.next().split())
id_train = []
x_train = np.zeros((n, m))
y_train = np.zeros(n) 
for i in range(n):
    rec_id, rec_x, rec_y = parse_record(inputf.next().split())
    id_train.append(rec_id)
    x_train[i, :] = rec_x
    y_train[i] = rec_y
# Test set
q = int(inputf.next())
id_test = []
x_test = np.zeros((q, m))
for i in range(q):
    rec_id, rec_x, _ = parse_record(inputf.next().split(), labeled = False)
    id_test.append(rec_id)
    x_test[i, :] = rec_x
        

## Train a small RandomForest -------------------------------------------------
rf = RandomForestClassifier(n_estimators = 100,
                            verbose = 0,
                            n_jobs = -1)
rf.fit(x_train, y_train)

## Predict the test set -------------------------------------------------------
y_test = zip(id_test, 
             map(lambda y: "+1" if y == 1.0 else "-1", rf.predict(x_test)))

## Output predictions ---------------------------------------------------------
for y_id, y in y_test:
    print y_id, y