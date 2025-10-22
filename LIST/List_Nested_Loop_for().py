rows = 3
cols = 3
identity_matrix = []

for i in range(rows):
    for j in range(cols):
        if j == i:
            identity_matrix.append(1)
        else:
            identity_matrix.append(0)
    print(identity_matrix)
    identity_matrix = []