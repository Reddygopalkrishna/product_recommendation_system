import numpy as np  # Import the numpy module for numerical operations

users = ["user1", "user2", "user3"]  # List of user names

products = ["laptop", "mouse", "monitor", "pen drive", "hard disk"]  # List of product names


uids = {}  # Dictionary to store user IDs
for i in range(len(users)):
    uids[users[i]] = i  

pids = {}  # Dictionary to store product IDs
for i in range(len(products)):
    pids[products[i]] = i  

print(uids, pids)  

prd_fq = np.zeros((len(users), len(products)))  # Create a 2D array to store the product frequency matrix
print(prd_fq)  # Print the product frequency matrix (initialized with zeros)


def reclist(uid):
    uid = uids[uid]  
    upids = prd_fq[uid, :]  # Get the product frequency for the given user from the product frequency matrix
    plist = np.argsort(upids)[::-1][:len(upids)]  # Sort the product frequency in descending order and get the indices
    plist = [products[p] for p in plist]  # Convert the sorted indices back to product names
    print(plist) 


def viewproduct(uid, pid):
    uid = uids[uid]  
    pid = pids[pid] 
    prd_fq[uid, pid] = prd_fq[uid, pid] + 1  # Increment the product frequency for the user and product combination
    print(prd_fq)  

uname = input("Enter user name:")  print(reclist(uname))  # Call the reclist function to get the recommended products for the given user

pname = input("Select one product:")  
viewproduct(uname, pname)  
