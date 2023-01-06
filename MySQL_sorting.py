import mysql.connector
cnx = mysql.connector.connect(user='root', password='***', #local DB password
                              host='127.0.0.1',
                              database='mahyar')
cursor = cnx.cursor()
query = 'SELECT * FROM personnel'
cursor.execute(query)
candidates = list(cursor)
for i in range (0, len(candidates)-1):
    for j in range (i, len(candidates)):
        if candidates[i][2] < candidates[j][2]:
            candidates[i], candidates[j] = candidates[j], candidates[i]
        elif candidates[i][2] == candidates[j][2]:
            if candidates[i][1] > candidates[j][1]:
                candidates[i], candidates[j] = candidates[j], candidates[i]
for (name, weight, height) in candidates:
    print (name, height, weight)
cnx.close()  