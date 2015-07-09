from fractions import gcd
def lcm(num1,num2):
	lcm1 = num1 * num2 /  gcd ( num1 , num2 )
	return lcm1
def lcmm(*args):
     return reduce(lcm, args)

def print_matrix (C):
	for idx in range(len(C)):
		print C[idx]
def BFS(C, F, source, sink):
    queue = [source]         # the BFS queue                 
    paths = {source: []}     # 1 path ending in the key
    while queue:

        u = queue.pop(0)     # next node to explore (expand) 
        for v in range(len(C)):   # for each possible next node
 
            # path from u to v?     and   not yet at v?
            if C[u][v] - F[u][v] > 0 and v not in paths:
                 paths[v] = paths[u] + [(u,v)]
                 if v == sink:
                      return paths[v]  # path ends in the key!

                 queue.append(v)   # go from v in the future 
    return None

def max_flow(C, source, sink):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)] # F is the flow matrix
    # residual capacity from u to v is C[u][v] - F[u][v]
    global path_flow 
    while True:
        path = BFS(C, F, source, sink)
        if not path: 
		break   # no path - we're done!
        edge_flows = [C[u][v]-F[u][v] for u,v in path]
        path_flow=min( edge_flows )
        
	
        for u,v in path: # traverse path to update flow
            F[u][v] += path_flow     # forward edge up 
            F[v][u] -= path_flow     # backward edge down 

    print_count = 0
    for u in range(matrix_size - 1):
	for v in range(matrix_size - 1):
	    if not u==0 and not v==matrix_size-1 and F[u][v] > 0:
	        got_job_idx = False
		got_frame_idx = False
		abc = ""
		fl = ""
		for key, value in mtx_idx_map.iteritems():
		    if value == u:
			abc = key
			got_job_idx = True

		    if value == v:
			f1 = key
			got_frame_idx = True

		if got_job_idx and got_frame_idx:
		   # print_count += 1			
		    print "in frame", f1
		    print "Job",abc,"has execution time of",F[u][v]  

    #print 'print_count:',print_count
    return sum([F[source][i] for i in range(n)])	
	
	 
		
period = []
exe = []
phs = []

def  read_input_file (table1):
 	  global period
	  global exe		 
          with open(table1, 'r') as f:
                  while True:
                          line = f.readline()
                          if not line:
                                  break
  
                          line = line.replace('(', '')
                          line = line.replace(')', '')
                          task_parameters = line.split(',')
  
                          if len(task_parameters) != 4:
                                 print 'invalid line'
                                 break
 
                          phs1 = float(task_parameters[0])
                          period1 = int(task_parameters[1])
                          exe1 = float(task_parameters[2])
                          deadline = int(task_parameters[3])
			  exe.append(exe1)
			  period.append(period1)     
			  phs.append(phs1)

read_input_file('table2.txt')
sys_util=0
for inf in range(0,len(period)):
	util=exe[inf]/period[inf]
	print "Utilization of task T(%d) is"% (inf+1), util 
	sys_util+=util
print "system utilisation is", sys_util
frameLt = []
newfr = []
newfr1 = []
vList = []
fNum = []
tstr1 = []
hyperPeriod = lcmm(*period)
print "hyperperiod",hyperPeriod
for h in range(1,hyperPeriod+1):
  if(hyperPeriod%h == 0):
    frameLt.append(h)  
for u in range(1,(len(frameLt))):
	check = 0
	for d in range(0,2):
   		if not(2*frameLt[u]-gcd(period[d],frameLt[u])<=period[d]): 
			check = 1
	if(0 == check):		
		newfr1.append(frameLt[u])
#print newfr
newfr.append(newfr1[8])
first_cons = []
for first in range(0,len(newfr)):
	if newfr[first]>=max(exe):
		first_cons.append(newfr[first])
print "the array of elements which satisfy first constraint as well are", first_cons


for r in reversed(range(0,len(newfr))):
	global matrix_size
	num_of_jobs=0
	num_of_minor_cycles = hyperPeriod / newfr[r]
	num_frames = hyperPeriod/newfr[r] 
	for i in range(0,len(period)):
		num_of_jobs+= hyperPeriod/period[i]
	matrix_size=2 + num_frames + num_of_jobs 

	C= [[0 for x in range(0,matrix_size)] for x in range(0,matrix_size)]
	job_init_idx = 1
	ind=0
	global job_mtx_idx
	global frame_mtx_idx
	global mtx_idx_map
	mtx_idx_map = {}
	for i in range(1,len(period)+1):
	    for k in range(1,(hyperPeriod/period[i-1])+1):
		abc= "j" + str(i)+'-' +str(k)
		ind+=1
		mtx_idx_map[abc] = ind
	        C[0][ind]=exe[i-1] 
	
	
	for k in range(1,num_of_minor_cycles+1): 
		
	     # if k>num_of_minor_cycles:
	#		k-=num_of_minor_cycles
	      ind+=1
	      f1= "f" +str(k)
	      mtx_idx_map[f1]=ind
	      C[ind][matrix_size-1]=newfr[r]
	      
			
	for i in range(1,len(period)+1):    
		startv1 = 0 + phs[i-1]
		endv1 = period[i-1] + phs[i-1]
		for k in range(1,(hyperPeriod/period[i-1])+1):
			abc= "j" + str(i)+'-' +str(k)
			
			startv2 = 0
			endv2 = newfr[r]
			fridx_start= int (startv1/newfr[r])
			fridx_end = int ((startv1 + period[i-1]) / newfr[r]) - 1

			num_of_minor_cycles = hyperPeriod / newfr[r]
			if fridx_start >= num_of_minor_cycles:
				fridx_start -= num_of_minor_cycles

			
			for k in range(1,2*num_of_minor_cycles+1): 
				
				
				if k>num_of_minor_cycles:
					k-=num_of_minor_cycles
				f1= "f" +str(k)
				
				if (startv2 >= startv1):
				     if endv2 <= endv1: 
					
					
					job_mtx_idx = mtx_idx_map[abc]
					frame_mtx_idx = mtx_idx_map[f1]
					C[job_mtx_idx][frame_mtx_idx] = newfr[r]
					
					
				startv2 = startv2 + newfr[r]
				endv2 = endv2 + newfr[r]
						
		        
			startv1 = startv1 + period[i-1]
			endv1 = endv1 + period[i-1]
	print "* Maximum Flow for frame size %d " % newfr[r], max_flow(C,0,matrix_size-1 )
