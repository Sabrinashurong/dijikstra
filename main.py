import re
from dijikstra import Graph

graph = Graph(200)
num1 = 29;num2 = 257
with open('inputData\input_random_%d_%d.txt'%(num1,num2),'r') as fo:
    j = 0
    for ar in fo:
        j = j+1
        ar = re.sub(r'\n', r'', ar)
        ar = re.split(r'\t', ar)
        v_start = int(ar[0])
        for i in range(1, len(ar)):
            if ar[i] != '':
                [v_end, v_value] = re.split(r',', ar[i])
                v_end = int(v_end);v_value = int(v_value);
                #print(v_start, v_end, v_value)
                graph.addEdge(v_start-1, v_end-1, v_value)


# Driver program to test the above functions

dist = graph.dijkstra(0)
print(dist)
with open('inputData\output_random_shurong_%d_%d.txt'%(num1,num2),'w') as fo:
    for i in [7,37,59,82,99,115,133,165,188,197]:
        fo.write(str(dist[i-1])+',')
