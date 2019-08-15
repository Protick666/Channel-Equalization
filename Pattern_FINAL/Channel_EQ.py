import numpy

def fetch(i,n):
    if i >=  n:
        return train_string[i-n:i]
    else:
        sub = train_string[0:i]
        p=""
        for j in range (1,n-i+1):
            p = p + "0"
        return p + sub

def val(i, n, sub):
    j = n - 1
    sum = 0
    for i in range(0,len(sub)):
        sum = sum + int(sub[i]) * weights[j]
        j = j - 1
    noise= numpy.random.normal(0, .1, size=1)
    sum = sum + noise[0]
    return sum


n = 3

train_string = "00000101001110010111011110100111001011010011100101110111"

train_array = numpy.zeros((len(train_string)+1))

conv_array = numpy.zeros((len(train_string)+1))

weights = numpy.random.rand((len(train_string)+1))

k = len(train_string)

for i in range (0,k):
    train_array[i+1] = int(train_string[i])

vis = {}
tot = 0
present_state = []
base_probability = {}

for i in range (0,k-n+1):
    tot = tot + 1
    sub = train_string[i:i+n]
    if sub not in vis:
        vis[sub] = 0
        present_state.append(sub)
    vis[sub] = vis[sub] + 1

for i in range (0,len(present_state)):
    base_probability[present_state[i]] = vis[present_state[i]]/tot
    #print(present_state[i],base_probability[present_state[i]])

out_going = {}
#no_as_source={}
possible_transitions=[]
transition_prob = {}

for i in range (0,k-n):
    sub1 = train_string[i:i+n]
    sub2 = train_string[i+1:i+1+n]
    sub = sub1 + sub2
    if sub not in out_going:
        out_going[sub] = 0
        possible_transitions.append(sub)
    out_going[sub] = out_going[sub] + 1

for i in range(0,len(possible_transitions)):
    full = possible_transitions[i]
    source = full[0:n]
    transition_prob[full] = out_going[full] / vis[source]
    #print(full,transition_prob[full])

offspring = {}

Mu = {}
Sigma = {}

for i in range(1,k+1):
    sub = fetch(i,n)
    conv_array[i] = val(i, n,sub )
    if sub not in offspring:
        offspring[sub] = []
    offspring[sub].append(conv_array[i])

for i in offspring:
    sum = 0
    for j in offspring[i]:
        sum = sum + j
    Mu[i] = sum / len(offspring[i])
    sum = 0
    for j in offspring[i]:
        sum = sum + (Mu[i] - j) * (Mu[i] - j)
    sum = sum/len(offspring[i])
    sum = sum ** .5
    Sigma[i] = sum
    print(i,Sigma[i])




















