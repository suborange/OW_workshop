# take the arrays now
# Front turn
# F1 - F9, 9 arrays for each face
# Up - 1,2,3
#Right - 1,4,7
#Down - 1,2,3 
#Left - 1,4,7

## TODO
# max array values - can have over 250 elements
# need to make sense of constants - i think the vars i have now should be constants.
# so need to make another array to hold all 216 values
# need to maybe add all the values into one array
# then can follow similar pattern, get index of the full array, of constant coordinates
# append in order of F1 1->2->3->4->1 -->> F2 1->2->3->4->1 -->> etc. 1-4, of 1-9.
# grab all 96 ( fukc) and append in front array?
# for loop, through full array, at that index ( in order of the front index array)
# full_arr[front_index_arr] += Vector(calcualted difference between destination, and this start)
# destination is in multiples of 4, so pass 1-4, then pass 5-8, then pass 9-12, to 33-36

## TODONE
# max array values - can have over 250 elements
# made sense of constants - the vars i have now should be constants.
# made another array to hold all 216 values
#  added all the values into one array
# made pattern for facing color and side colors. got index of cube coords @ unique positions from constants
# append in order, now have index relating to all those constants
# loop through and add the vector differences between each of the given cubies and 4 vector poisipositions


##########################################################################################################################
def mod_sides(face, start, shift2, shift3):
        # for the other faces:
    # Down face:
    findex=1;
    face_num=start;
    for i in range(0,12,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
##        print(i);
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4            
            face_num = shift2; # move to next face and its 4 vectors
        if ( face_num != shift3 and i >=  7): # must be every 4 loops - face 3
            face_num = shift3
            


            
##########################################################################################################################    
# find the differences for the front turn?
# front turn rule
def mod_front_turn(face, face_num):
    #  vector destination - vector start
    # print "modify glob"
    findex = 1;

    # for the white face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:
    # Down face:
    mod_sides("Down_", 1,2,3);

    # Left face:
    mod_sides("Left_", 3,6,9);

    # Up face:
    mod_sides("Up_", 7,8,9);

    # Right face:
    mod_sides("Right_", 1,4,7);

    
##########################################################################################################################    
# find the differences for the right turn?
# right turn rule
def mod_right_turn(face, face_num):
    #  vector destination - vector start
    # print "modify global."
    findex = 1;

    # for the red face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:
    # Down face:
    mod_sides("Down_", 3,6,9);

    # Front  face:
    mod_sides("Front_", 3,6,9);

    # Up face:
    mod_sides("Up_", 3,6,9);

    # Back face:
    mod_sides("Back_", 1,4,7);

##########################################################################################################################    
# find the differences for the down turn?
# down turn rule
def mod_down_turn(face, face_num):
    #  vector destination - vector start
    # print "modify global."
    findex = 1;

    # for the green face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:

    # Front  face:
    mod_sides("Front_", 7,8,9);

     # Right face:
    mod_sides("Right_", 7,8,9);

    # Back face:
    mod_sides("Back_", 7,8,9);

   # Left face:
    mod_sides("Left_", 7,8,9);


##########################################################################################################################    
# find the differences for the up turn?
# up turn rule
def mod_up_turn(face, face_num):
    #  vector destination - vector start
    # print "modify global."
    findex = 1;

    # for the blue face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:

    # Front  face:
    mod_sides("Front_", 1,2,3);

   # Left face:
    mod_sides("Left_", 1,2,3);
    
     # Back face:
    mod_sides("Back_", 1,2,3);

    # Right face:
    mod_sides("Right_", 1,2,3);

##########################################################################################################################    
# find the differences for the left turn?
# left turn rule
def mod_left_turn(face, face_num):
    #  vector destination - vector start
    # print "modify global."
    findex = 1;

    # for the orange face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:
    # Up face:
    mod_sides("Up_", 1,4,7);

    # Front  face:
    mod_sides("Front_", 1,4,7);

    # Up face:
    mod_sides("Down_", 1,4,7);

    # Back face:
    mod_sides("Back_", 3,6,9);

##########################################################################################################################    
# find the differences for the back turn?
# back turn rule
def mod_back_turn(face, face_num):
    #  vector destination - vector start
    # print "modify glob"
    findex = 1;

    # for the black face
    for i in range(0,36,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:
    # Down face:
    mod_sides("Down_", 7,8,9);

    # Right face:
    mod_sides("Right_", 3,6,9);

    # Up face:
    mod_sides("Up_", 1,2,3);

    # Left face:
    mod_sides("Left_", 1,4,7);    
    
        
##########################################################################################################################
### FOR CLOCKWISE - DEFAULT NOTATION - NOT INVERSE(inverse should switch start and end? - no will pass different faces in.. too much work...)
# to pass the face and cubie value
# finding the difference between this vector and its destination.
# for front faces, 1->2->3->4->1
# with cubie value, 
def vector_difference(vector_face_start, vector_face_end):
    # find the difference between the vectors that need to change.
    # end - start vectors = difference to print out.
    # go from vector position Front
    # face 3 pos 2 - face 1 pos 1
    difference = [0,0,0];
    for i in range(0,3,1):
        difference[i] = round((vector_face_end[i] - vector_face_start[i]), 2)


# this is where i could loop the additions ( well encapsulating this whole statement)

##    return "Vector(" + str(difference[0])+ ", " + str(difference[1])+ ",  " + str(difference[2]) + ");";
    return "Vector(" + str(difference[0]/4)+ ", " + str(difference[1]/4)+ ",  " + str(difference[2]/4) + ");";


##########################################################################################################################
def glob_coords(index):
    # print  initial part, index from 1-84?
    return"Global.Cube_coords[Global.position_index["+str(index)+"]] += ";
    
##########################################################################################################################
# for the front facing side of a turn. given white face -> front turn, given red -> right turn, given green -> down turn
# given a face, calcualtes for that side, and then calls the corresponding side functions
def calc_facing_side(face_vector, position_index ):
    # split into faces cant figure out algorithm for shuffling around
    F1 =[0];
    F2 =[0];
    F3 =[0];
    F4 =[0];
    F5 =[0];
    F6 =[0];
    F7 =[0];
    F8 =[0];
    F9 =[0];

# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?

    for m in range(1,5,1):
        F1.append(face_vector[m]);
        F2.append(face_vector[m+4]);
        F3.append(face_vector[m+8]);
        F4.append(face_vector[m+12]);
        F5.append(face_vector[m+16]);
        F6.append(face_vector[m+20]);
        F7.append(face_vector[m+24]);
        F8.append(face_vector[m+28]);
        F9.append(face_vector[m+32]);
        
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    # 5,6,7,8 are position 2

# face 1    
    # position index is incremented
    # need to go from pos1-> 4 somehow - loop 9 times for each face
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F1[posA], F3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1
# face 2
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F2[posA], F6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1


# face 3
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F3[posA], F9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1


# face 4
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F4[posA], F2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # face 5
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F5[posA], F5[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

# face 6
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F6[posA], F8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

# face 7
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F7[posA], F1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

# face 8
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F8[posA], F4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1


# face 9
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F9[posA], F7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    return position_index;            
##
############################################################################################################################
## RIGHT SIDE - can swap the for loop order? to change the faces? switch colors.. try it out? so much more code tho.. affect the engine how?
############################################################################################################################
def calc_right_sides(green, white, blue, black, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around
  
    D3 =[0];
    D6 =[0];
    D9 =[0];
    F3 =[0];
    F6 =[0];
    F9 =[0];
    U3 =[0];
    U6 =[0];
    U9 =[0];
    B1 =[0];
    B4 =[0];
    B7 =[0];

# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?
# 1 - m
# 2 - m + 4
# 3 - m + 8
# 6 - m + 20
# 9 - m + 32
    for m in range(1,5,1):
        D3.append(green[m+8]);
        D6.append(green[m+20]);
        D9.append(green[m+32]);
        F3.append(white[m+8]);
        F6.append(white[m+20]);
        F9.append(white[m+32]);
        U3.append(blue[m+8]);
        U6.append(blue[m+20]);
        U9.append(blue[m+32]);        
        B1.append(black[m]);
        B4.append(black[m+12]);
        B7.append(black[m+24]);        
    
    # do green - bottom sides, 3->6->9
    # green 3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D3[posA], F3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4
       

                # do green - bottom sides, 3->6->9
    # green 6
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D6[posA], F6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4
       

    # do green - bottom sides, 3->6->9
    # green 9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D9[posA], F9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4
    

    # do white  - front sides, 3->6->9
    # white 3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F3[posA], U3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
      

    # do white  - front sides, 3->6->9
    # white 6
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F6[posA], U6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
               

    # do white - front sides, 3->6->9
    # white 9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F9[posA], U9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1            

    # do blue - up sides, 3->6->9
    # blue 3
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos3
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U3[posA], B7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1

    ## do blue - up sides, 3->6->9
    # blue 6
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos3
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U6[posA], B4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1

    # do blue - up sides, 3->6->9
    # blue 9
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos3
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U9[posA], B1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1            

    # do black - back sides, 1->4->7
    # black 1
    posA = 1; # start on pos1, moving to  pos3
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B1[posA], D9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1


    # do black - back sides, 1->4->7
    # black 4
    posA = 1; # start on pos1, moving to  pos3
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B4[posA], D6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1

    # do black - back sides, 1->4->7
    # black 7
    posA = 1; # start on pos1, moving to  pos3
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B7[posA], D3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if ( posB >=5):
            posB=1; # 4->1            

############################################################################################################################
## DOWN SIDE - can swap the for loop order? to change the faces? switch colors.. try it out? so much more code tho.. affect the engine how?
############################################################################################################################
def calc_down_sides(white, red, black, orange, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around
  
    F7 =[0];
    F8 =[0];
    F9 =[0];
    R7 =[0];
    R8 =[0];
    R9 =[0];
    B7 =[0];
    B8 =[0];
    B9 =[0];
    L7 =[0];
    L8 =[0];
    L9 =[0];


# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?
# 1 - m
# 2 - m + 4
# 3 - m + 8
# 6 - m + 20
# 9 - m + 32
    for m in range(1,5,1):
        F7.append(white[m+24]);
        F8.append(white[m+28]);
        F9.append(white[m+32]);
        R7.append(red[m+24]);
        R8.append(red[m+28]);
        R9.append(red[m+32]);
        B7.append(black[m+24]);
        B8.append(black[m+28]);
        B9.append(black[m+32]);
        L7.append(orange[m+24]);
        L8.append(orange[m+28]);
        L9.append(orange[m+32]);        
    
    # do white - front sides, 7->8->9
    # front 7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F7[posA], R7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 7->8->9
    # front 8
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F8[posA], R8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 7->8->9
    # front 9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F9[posA], R9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        

    # do red - right sides, 7->8->9
    # right  7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R7[posA], B7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do red - right sides, 7->8->9
    # right  8
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R8[posA], B8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do red - right sides, 7->8->9
    # right  9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R9[posA], B9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        

    # do black - back sides, 7->8->9
    # black  7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B7[posA], L7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do black - back sides, 7->8->9
    # black  8
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B8[posA], L8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do black - back sides, 7->8->9
    # black  9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B9[posA], L9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 7->8->9
    # orange  7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L7[posA], F7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 7->8->9
    # orange  8
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L8[posA], F8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 7->8->9
    # orange  9
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L9[posA], F9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4                
           

############################################################################################################################
## UP SIDE - can swap the for loop order? to change the faces? switch colors.. try it out? so much more code tho.. affect the engine how?
############################################################################################################################
def calc_up_sides(white, orange, black, red, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around
  
    F1 =[0];
    F2 =[0];
    F3 =[0];
    L1 =[0];
    L2 =[0];
    L3 =[0];
    B1 =[0];
    B2 =[0];
    B3 =[0];
    R1 =[0];
    R2 =[0];
    R3 =[0];    



# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?
# 1 - m
# 2 - m + 4
# 3 - m + 8
# 6 - m + 20
# 9 - m + 32
    for m in range(1,5,1):
        F1.append(white[m]);
        F2.append(white[m+4]);
        F3.append(white[m+8]);
        L1.append(orange[m]);
        L2.append(orange[m+4]);
        L3.append(orange[m+8]);
        B1.append(black[m]);
        B2.append(black[m+4]);
        B3.append(black[m+8]);
        R1.append(red[m]);
        R2.append(red[m+4]);
        R3.append(red[m+8]);        
    
    # do white - front sides, 1->2->3
    # front 1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F1[posA], L1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 1->2->3
    # front 2
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F2[posA], L2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 1->2->3
    # front 3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F3[posA], L3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 1->2->3
    # orange  1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L1[posA], B1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 1->2->3
    # orange  2
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L2[posA], B2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do orange - left sides, 1->2->3
    # orange  3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L3[posA], B3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4             
    
    # do black - back sides, 1->2->3
    # black  1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B1[posA], R1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do black - back sides, 1->2->3
    # black  2
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B2[posA], R2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do black - back sides, 1->2->3
    # black  3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B3[posA], R3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        


# do red - right sides, 1->2->3
    # right  1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R1[posA], F1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do red - right sides, 1->2->3
    # right  2
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R2[posA], F2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do red - right sides, 1->2->3
    # right  3
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R3[posA], F3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        
    
############################################################################################################################
## LEFT SIDE - can swap the for loop order? to change the faces? switch colors.. try it out? so much more code tho.. affect the engine how?
############################################################################################################################
def calc_left_sides(blue, white, green, black, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around

    U1 =[0];
    U4 =[0];
    U7 =[0];
    F1 =[0];
    F4 =[0];
    F7 =[0];
    D1 =[0];
    D4 =[0];
    D7 =[0];     
    B3 =[0];
    B6 =[0];
    B9 =[0];



# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?
# 1 - m
# 2 - m + 4
# 3 - m + 8
# 6 - m + 20
# 9 - m + 32
    for m in range(1,5,1):
        U1.append(blue[m]);
        U4.append(blue[m+12]);
        U7.append(blue[m+24]);
        F1.append(white[m]);
        F4.append(white[m+12]);
        F7.append(white[m+24]);
        D1.append(green[m]);
        D4.append(green[m+12]);
        D7.append(green[m+24]);        
        B3.append(black[m+8]);
        B6.append(black[m+20]);
        B9.append(black[m+32]);        
    
    # do blue - bottom sides, 1->4->7
    # blue 1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U1[posA], F1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do blue - bottom sides, 1->4->7
    # blue 4
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U4[posA], F4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        

    # do blue - bottom sides, 1->4->7
    # blue 7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U7[posA], F7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4       

    # do white - front sides, 1->4->7
    # white 1
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F1[posA], D1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 1->4->7
    # white 4
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F4[posA], D4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4

    # do white - front sides, 1->4->7
    # white 7
    posA = 1; # start on pos1, moving to  pos1
    posB = 1; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(F7[posA], D7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 1->2->3->4        

    # do green - bottom sides, 1->4->7
    # green 1
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D1[posA], B9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1

    # do green - bottom sides, 1->4->7
    # green 4
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D4[posA], B6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1

    # do green - bottom sides, 1->4->7
    # green 7
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D7[posA], B3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1            

    # do black  - back sides, 3->6->9
    # black 3
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B3[posA], U7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1          

      

      # do black  - back sides, 3->6->9
    # black 6
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B6[posA], U4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1  

    # do black  - back sides, 3->6->9
    # black 9
    posA = 1; # start on pos1, moving to  pos1
    posB = 3; # end on pos1
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(B9[posA], U1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 3->4->1->2
        if posB >= 5:
            posB = 1; # reset 4->1  
            

############################################################################################################################
## BACK SIDE
############################################################################################################################
def calc_back_sides(green, red, blue, orange, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around
    D7 =[0];
    D8 =[0];
    D9 =[0];
    R3 =[0];
    R6 =[0];
    R9 =[0];
    U1 =[0];
    U2 =[0];
    U3 =[0];
    L1 =[0];
    L4 =[0];
    L7 =[0];

# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?

    for m in range(1,5,1):
        D7.append(green[m+24]);
        D8.append(green[m+28]);
        D9.append(green[m+32]);
        R3.append(red[m+8]);
        R6.append(red[m+20]);
        R9.append(red[m+32]);
        U1.append(blue[m]);
        U2.append(blue[m+4]);
        U3.append(blue[m+8]);        
        L1.append(orange[m]);
        L4.append(orange[m+12]);
        L7.append(orange[m+24]);        
    
    # do green - bottom sides, 7->8->9
    # green 7 
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D7[posA], R9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do green - bottom sides, 7->8->9
    # green 8
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D8[posA], R6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do green - bottom sides, 7->8->9
    # green 9
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D9[posA], R3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

# do red - right sides, 3->6->9
    # red 3
    posA = 1; # start on pos1, moving to  pos2
    posB = 4; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R3[posA], U1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

# do red - right sides, 3->6->9
    # red 6
    posA = 1; # start on pos1, moving to  pos2
    posB = 4; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R6[posA], U2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

# do red - right sides, 3->6->9
    # red 9
    posA = 1; # start on pos1, moving to  pos2
    posB = 4; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R9[posA], U3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1            

           

    # do blue - up sides, 1->2->3
    # blue 1
    posA = 1; # start on pos1, moving to  pos2
    posB = 4 # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U1[posA], L7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

    # do blue - up sides, 1->2->3
    # blue 2
    posA = 1; # start on pos1, moving to  pos2
    posB = 4 # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U2[posA], L4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

    # do blue - up sides, 1->2->3
    # blue 3
    posA = 1; # start on pos1, moving to  pos4
    posB = 4 # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U3[posA], L1[posB]));
    
        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1            
         

# do orange - left sides, 1->4->7
    # orange 1
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L1[posA], D7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

# do orange - left sides, 1->4->7
    # orange 4
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L4[posA], D8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1

# do orange - left sides, 1->4->7
    # orange 7
    posA = 1; # start on pos1, moving to  pos4
    posB = 4; # end on pos4
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L7[posA], D9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 4->1->2->3
        if ( posB >=5):
            posB=1; # 4->1            
   

############################################################################################################################
## FRONT SIDE
############################################################################################################################
def calc_front_sides(green, orange, blue, red, position_index):
    # loop to grab the vectors like before for each face
        # split into faces cant figure out algorithm for shuffling around
    D1 =[0];
    D2 =[0];
    D3 =[0];
    L3 =[0];
    L6 =[0];
    L9 =[0];
    U7 =[0];
    U8 =[0];
    U9 =[0];
    R1 =[0];
    R4 =[0];
    R7 =[0];

# arrays with position 1, 2,3,4 for each face.
# then pass in pos1[1], pos 2[3]. start and end?

    for m in range(1,5,1):
        D1.append(green[m]);
        D2.append(green[m+4]);
        D3.append(green[m+8]);
        L3.append(orange[m+8]);
        L6.append(orange[m+20]);
        L9.append(orange[m+32]);
        U7.append(blue[m+24]);
        U8.append(blue[m+28]);
        U9.append(blue[m+32]);        
        R1.append(red[m]);
        R4.append(red[m+12]);
        R7.append(red[m+24]);        
    
    # do green - bottom sides, 1->2->3->1
    # green 1 
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D1[posA], L3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

                # do green - bottom sides, 1->2->3->1
    # green 2
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D2[posA], L6[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do green - bottom sides, 1->2->3
    # green 3
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(D3[posA], L9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do orange - left sides, 3->6->9
    # orange 3
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L3[posA], U9[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do orange - left sides, 3->6->9
    # orange 6
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L6[posA], U8[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1            

    # do orange - left sides, 3->6->9
    # orange 9
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(L9[posA], U7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1            

    # do blue - up sides, 7->8->9
    # blue 7
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U7[posA], R1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do blue - up sides, 7->8->9
    # blue 8
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U8[posA], R4[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do blue - up sides, 7->8->9
    # blue 9
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(U9[posA], R7[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1               

    # do red - right sides, 1->4->7
    # red 1
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R1[posA], D3[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do red - right sides, 1->4->7
    # red 4
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R4[posA], D2[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1

    # do red - right sides, 1->4->7
    # red 7
    posA = 1; # start on pos1, moving to  pos2
    posB = 2; # end on pos2
    for n in range (0,4,1):
        # print the first difference.
        position_index+=1; # next point
        print( glob_coords(position_index) + vector_difference(R7[posA], D1[posB]));

        posA+=1; # go 1->2->3->4
        posB+=1; # go 2->3->4->1
        if ( posB >=5):
            posB=1; # 4->1 
            

###########################################################
## CONSTANTS
###########################################################            

white_vector =  [[], [-0.1, 20, 0], [-0.1, 20, 3], [-0.1, 17, 3], [-0.1, 17, 0], [-0.1, 20, 3.5], [-0.1, 20, 6.5], [-0.1, 17, 6.5], [-0.1, 17, 3.5], [-0.1, 20, 7], [-0.1, 20, 10], [-0.1, 17, 10], [-0.1, 17, 7], [-0.1, 16.5, 0], [-0.1, 16.5, 3], [-0.1, 13.5, 3], [-0.1, 13.5, 0], [-0.1, 16.5, 3.5], [-0.1, 16.5, 6.5], [-0.1, 13.5, 6.5], [-0.1, 13.5, 3.5], [-0.1, 16.5, 7], [-0.1, 16.5, 10], [-0.1, 13.5, 10], [-0.1, 13.5, 7], [-0.1, 13, 0], [-0.1, 13, 3], [-0.1, 10, 3], [-0.1, 10, 0], [-0.1, 13, 3.5], [-0.1, 13, 6.5], [-0.1, 10, 6.5], [-0.1, 10, 3.5], [-0.1, 13, 7], [-0.1, 13, 10], [-0.1, 10, 10], [-0.1, 10, 7]]
green_vector = [[], [0, 9.9, 0], [0, 9.9, 3], [3, 9.9, 3], [3, 9.9, 0], [0, 9.9, 3.5], [0, 9.9, 6.5], [3, 9.9, 6.5], [3, 9.9, 3.5], [0, 9.9, 7], [0, 9.9, 10], [3, 9.9, 10], [3, 9.9, 7], [3.5, 9.9, 0], [3.5, 9.9, 3], [6.5, 9.9, 3], [6.5, 9.9, 0], [3.5, 9.9, 3.5], [3.5, 9.9, 6.5], [6.5, 9.9, 6.5], [6.5, 9.9, 3.5], [3.5, 9.9, 7], [3.5, 9.9, 10], [6.5, 9.9, 10], [6.5, 9.9, 7], [7, 9.9, 0], [7, 9.9, 3], [10, 9.9, 3], [10, 9.9, 0], [7, 9.9, 3.5], [7, 9.9, 6.5], [10, 9.9, 6.5], [10, 9.9, 3.5], [7, 9.9, 7], [7, 9.9, 10], [10, 9.9, 10], [10, 9.9, 7]]
orange_vector = [[], [10, 20, -0.01], [7, 20, -0.01], [7, 17, -0.01], [10, 17, -0.01], [6.5, 20, -0.01], [3.5, 20, -0.01], [3.5, 17, -0.01], [6.5, 17, -0.01], [3, 20, -0.01], [0, 20, -0.01], [0, 17, -0.01], [3, 17, -0.01], [10, 16.5, -0.01], [7, 16.5, -0.01], [7, 13.5, -0.01], [10, 13.5, -0.01], [6.5, 16.5, -0.01], [3.5, 16.5, -0.01], [3.5, 13.5, -0.01], [6.5, 13.5, -0.01], [3, 16.5, -0.01], [0, 16.5, -0.01], [0, 13.5, -0.01], [3, 13.5, -0.01], [10, 13, -0.01], [7, 13, -0.01], [7, 10, -0.01], [10, 10, -0.01], [6.5, 13, -0.01], [3.5, 13, -0.01], [3.5, 10, -0.01], [6.5, 10, -0.01], [3, 13, -0.01], [0, 13, -0.01], [0, 10, -0.01], [3, 10, -0.01]]

red_vector =   [[], [0, 20, 10.09], [3, 20, 10.09], [3, 17, 10.09], [0, 17, 10.09], [3.5, 20, 10.09], [6.5, 20, 10.09], [6.5, 17, 10.09], [3.5, 17, 10.09], [7, 20, 10.09], [10, 20, 10.09], [10, 17, 10.09], [7, 17, 10.09], [0, 16.5, 10.09], [3, 16.5, 10.09], [3, 13.5, 10.09], [0, 13.5, 10.09], [3.5, 16.5, 10.09], [6.5, 16.5, 10.09], [6.5, 13.5, 10.09], [3.5, 13.5, 10.09], [7, 16.5, 10.09], [10, 16.5, 10.09], [10, 13.5, 10.09], [7, 13.5, 10.09], [0, 13, 10.09], [3, 13, 10.09], [3, 10, 10.09], [0, 10, 10.09], [3.5, 13, 10.09], [6.5, 13, 10.09], [6.5, 10, 10.09], [3.5, 10, 10.09], [7, 13, 10.09], [10, 13, 10.09], [10, 10, 10.09], [7, 10, 10.09]]
blue_vector = [[], [10, 20.1, 0], [10, 20.1, 3], [7, 20.1, 3], [7, 20.1, 0], [10, 20.1, 3.5], [10, 20.1, 6.5], [7, 20.1, 6.5], [7, 20.1, 3.5], [10, 20.1, 7], [10, 20.1, 10], [7, 20.1, 10], [7, 20.1, 7], [6.5, 20.1, 0], [6.5, 20.1, 3], [3.5, 20.1, 3], [3.5, 20.1, 0], [6.5, 20.1, 3.5], [6.5, 20.1, 6.5], [3.5, 20.1, 6.5], [3.5, 20.1, 3.5], [6.5, 20.1, 7], [6.5, 20.1, 10], [3.5, 20.1, 10], [3.5, 20.1, 7], [3, 20.1, 0], [3, 20.1, 3], [0, 20.1, 3], [0, 20.1, 0], [3, 20.1, 3.5], [3, 20.1, 6.5], [0, 20.1, 6.5], [0, 20.1, 3.5], [3, 20.1, 7], [3, 20.1, 10], [0, 20.1, 10], [0, 20.1, 7]]
black_vector = [[], [10.1, 20, 10], [10.1, 20, 7], [10.1, 17, 7], [10.1, 17, 10], [10.1, 20, 6.5], [10.1, 20, 3.5], [10.1, 17, 3.5], [10.1, 17, 6.5], [10.1, 20, 3], [10.1, 20, 0], [10.1, 17, 0], [10.1, 17, 3], [10.1, 16.5, 10], [10.1, 16.5, 7], [10.1, 13.5, 7], [10.1, 13.5, 10], [10.1, 16.5, 6.5], [10.1, 16.5, 3.5], [10.1, 13.5, 3.5], [10.1, 13.5, 6.5], [10.1, 16.5, 3], [10.1, 16.5, 0], [10.1, 13.5, 0], [10.1, 13.5, 3], [10.1, 13, 10], [10.1, 13, 7], [10.1, 10, 7], [10.1, 10, 10], [10.1, 13, 6.5], [10.1, 13, 3.5], [10.1, 10, 3.5], [10.1, 10, 6.5], [10.1, 13, 3], [10.1, 13, 0], [10.1, 10, 0], [10.1, 10, 3]]


##########################################################################################################################
def front_turn():
    print_prefix("Front turn - subroutine with animation","0", "Front");
        ## FRONT
    # modify the position array first for the front turn?
    mod_front_turn("Front_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(white_vector, position_index);
    
    # now finish up the rest of the sides - red, green, orange, blue for white front
    calc_front_sides(green_vector, orange_vector, blue_vector, red_vector, position_index);
    print("Wait(0.09, Ignore Condition);");
    print("End;");

##########################################################################################################################
def right_turn():
    print_prefix("Right turn - subroutine with animation", "1", "Right");    
        ## RIGHT
    # modify the position array first for the right turn?
    mod_right_turn("Right_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(red_vector, position_index);
    
    # now finish up the rest of the sides - red, green, orange, blue for white front
    calc_right_sides(green_vector, white_vector, blue_vector, black_vector, position_index);
    print("Wait(0.09, Ignore Condition);")
    print("End;");

##########################################################################################################################
def down_turn():
    print_prefix("Down turn - subroutine with animation", "2", "Down");    
        ## DOWN
    # modify the position array first for the down turn?
    mod_down_turn("Down_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(green_vector, position_index);
    
    # now finish up the rest of the sides - red, green, orange, blue for white front
    calc_down_sides(white_vector, red_vector, black_vector, orange_vector, position_index);
    print("Wait(0.09, Ignore Condition);")
    print("End;");



##########################################################################################################################
def up_turn():
    print_prefix("Up turn - subroutine with animation", "3", "Up");    
        ## UP
    # modify the position array first for the up turn?
    mod_up_turn("Up_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(blue_vector, position_index);
    
    # now finish up the rest of the sides - white, orange, black, red
    calc_up_sides(white_vector, orange_vector, black_vector, red_vector, position_index);
    print("Wait(0.09, Ignore Condition);")
    print("End;");


##########################################################################################################################
def left_turn():
    print_prefix("Left turn - subroutine with animation", "4", "Left");    
        ## LEFT
    # modify the position array first for the left turn?
    mod_left_turn("Left_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(orange_vector, position_index);
    
    # now finish up the rest of the sides - blue, white, green, black
    calc_left_sides(blue_vector, white_vector, green_vector, black_vector, position_index);
    print("Wait(0.09, Ignore Condition);");
    print("End;");

##########################################################################################################################
def back_turn():
    print_prefix("Back turn - subroutine with animation","5", "Back");
        ## BACK
    # modify the position array first for the back turn?
    mod_back_turn("Back_", 1);
    # prints modifiying constants

    # continue with calculations now, using position index as done in the past.
    position_index=0;
    # keep track of position index?
    print("For Global Variable(turn_counter, 0, 4, 1);");
    # should work for any side. 
    position_index = calc_facing_side(black_vector, position_index);
    
    # now finish up the rest of the sides - red, green, orange, blue for white front
    calc_back_sides(green_vector, red_vector, blue_vector, orange_vector, position_index);
    print("Wait(0.09, Ignore Condition);");
    print("End;");    
    
##########################################################################################################################
##########################################################################################################################
def print_prefix(comment, sub_num, sub_name):
    print("subroutines\n{\n\t"+ sub_num + ": " +  sub_name + "\n}");
    print("rule(\""+ comment+ "\")\n{\n\tevent\n\t{\n\t\tSubroutine;\n\t\t"+ sub_name+ ";\n\t}\n\n\tactions\n\t{");
# would have to type out 84 of these.. yikes.. need to reconsider the ordering? maybe store the array by face.. every 4 is another face.. its at least more mathy
# F1 - 1 and F3 - 2
#vector_difference(white_vector[1], white vector[3]); # + 4?
## + 4?

##########################################################################################################################
def main():

    # call front
##    front_turn();
##    right_turn();
##    down_turn();
##    up_turn();
##    left_turn();
    back_turn();

    print("\t\tFor Global Variable(remove_counter, Count Of(Global.position_index), 0, -1);");
    print("\t\t\tModify Global Variable(position_index, Remove From Array By Index, Global.remove_counter); ");
    print("End;");
    print("Global.remove_counter = 0;");
##    print("Create HUD Text(All Players(All Teams), Custom String(\"TURN DONE\"), Null, Null, Left, 0, Color(Gray), Color(White), Color(White), Visible To and String, Default Visibility);");
          
    print("\t}\n}");
    
    


if __name__ == "__main__":
    main();
    

##########################################################################################################################
## crap
##
##              #
##    # modify the position array first for the front turn?
##    mod_front_turn("Front_", 1);
##    # prints modifiying constants
##
##    # continue with calculations now, using position index as done in the past.
##    position_index=0
##    # keep track of position index?
##    print("For Global Variable(turn_counter, 0, 4, 1);");
##    position_index = calc_facing_side(white_vector, position_index);
##    
##    # now finish up the rest of the sides - red, green, orange, blue for white front
##    calc_front_sides(green_vector, orange_vector, blue_vector, red_vector, position_index);
##    print("Wait(0.150, Ignore Condition);")
##    print("End;");

