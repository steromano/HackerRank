with open("input01.txt") as inputf:
    n, m = map(int, inputf.next().split())
    id_train = []
    x_train = np.zeros((n, m))
    y_train = np.zeros(n) 
    def parse_record(line, labeled = True):
        rec_id = line[0]
        rec_y = line[1] if labeled else None
        k = 2 if labeled else 1
        rec_x = map(lambda x: x.split(":")[1], line[k:])
        return rec_id, rec_x, rec_y
    for i in range(n):
        rec_id, rec_x, rec_y = parse_record(inputf.next().split())
        id_train.append(rec_id)
        x_train[i, :] = rec_x
        y_train[i] = rec_y
    q = int(inputf.next())
    id_test = []
    x_test = np.zeros((q, m))
    for i in range(q):
        rec_id, rec_x, _ = parse_record(inputf.next().split(), labeled = False)
        id_test.append(rec_id)
        x_test[i, :] = rec_x
        
with open("output01.txt") as outputf:
    y_test_actual = map(lambda row: row.split(), outputf)
    

def accuracy(y1s, y2s):
    n = float(len(y1s))
    return sum(y1 == y2 for (_1, y1), (_2, y2) in zip(y1s, y2s))/n

print accuracy(y_test_actual, y_test)