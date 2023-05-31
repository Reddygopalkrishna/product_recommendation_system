import numpy as np       # numpy module

users = ["user1","user2","user3"]  # users

products = ["laptop","mouse","monitor","pen drive","hard disk"] # products

uids = {} #dict

for i in range(len(users)):
  uids[users[i]]=i

pids = {} # dict

for i in range(len(products)):
  pids[products[i]]=i

print(uids, pids)

prd_fq = np.zeros((len(users),len(products)) )   # Product frequency 
print(prd_fq)


def reclist(uid):
  uid = uids[uid]
  upids = prd_fq[uid, :]
  plist = np.argsort(upids)[::-1][:len(upids)]
  plist = [products[p] for p in plist]
  print(plist)
  

def viewproduct(uid, pid):
  uid = uids[uid]
  pid = pids[pid]
  prd_fq[uid, pid] = prd_fq[uid, pid] + 1
  print(prd_fq)


uname = input("Enter user name:")
print(reclist(uname))

pname = input("Select one product:")
viewproduct(uname, pname)

