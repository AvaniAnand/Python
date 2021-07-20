#########################################
##This is my_lists file
#########################################
print("######################")
print("##Lists")
print("######################")

# we have sttudent ids and we want to see their attendance
# 108, 37, 6007, 58, 900, 605
# list[member 0, member 1, member 2, member 3,    -----, member last]
# list[index0, index1, index2, .... , index last]
missing_stu_list = [108, 37, 6007, 58, 900, 605]

#some of basics about lists
#1- len(list_name) returns the totlal elements of the list, i.e. the length of the list
#for example len(missing_stu_list)

#access an element at a position/index
# list_name[index]
#n_idx = 2
#n_elem  = missing_stu_list[n_idx]

#print the list

print("######################")
print("##Part0 -- how to print the list")
print("######################")

print("print the complete missing_stu_list")
print(missing_stu_list[:])

print("print elements 2nd to 4th")
print(missing_stu_list[1:4])


#my student id is 58
#my student id is 200

#how to get the list members
print("######################")
print("##Part1 -- how to get the list members")
print("######################")

#for item in list_name:
for item in missing_stu_list:
    print("An item in the sample list is ", item)
    

#another way
print("######################")
print("##Part2 -- another way to get list members")
print("######################")

# len function return the total members of a list
total_members = len(missing_stu_list)
print("missing_stu_list members are " + str(total_members))

curr_indx = 0
# < less than
# 
while(curr_indx < total_members):
    curr_member = missing_stu_list[curr_indx]
    print (" At index " + str(curr_indx) + " missing id is " + str(curr_member))
    
    curr_indx +=1
    #curr_indx = curr_indx + 1

print("######################")
print("##Part3 -- simple way to get both the index and the item")
print("######################")

# If you need both the index and the item, use the enumerate function:
for index, item in enumerate(missing_stu_list):
    print ("The element index is ",index," and the value is ", item)


    
#add a member to a list
print("######################")
print("##Part4 -- add a member to a list")
print("######################")
new_member = 100

missing_stu_list.append(new_member)
#missing_stu_list.append(10009)

curr_indx = 0
total_members = len(missing_stu_list)
print("Updated list is ")

print("missing_stu_list members are " + str(total_members))

while(curr_indx < total_members):
    curr_member = missing_stu_list[curr_indx]
    print (" at index " + str(curr_indx) + " missing id is " + str(curr_member))
    
    curr_indx +=1
    
print("######################")
print("##Part5 -- remove a member from a list")
print("######################")   

#remove a member 
rmv_member = 37

if rmv_member in missing_stu_list:
    print("rmv_member " + str(rmv_member) + " exists in the list")
    missing_stu_list.remove(rmv_member)

#please try pop function
#missing_stu_list.append(10009)

curr_indx = 0
total_members = len(missing_stu_list)
print("Updated list is ")

print("missing_stu_list members are " + str(total_members))

while(curr_indx < total_members):
    curr_member = missing_stu_list[curr_indx]
    print (" at index " + str(curr_indx) + " missing id is " + str(curr_member))
    
    curr_indx +=1