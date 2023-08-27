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

"""
Global.BD = 0;
# create hud with AY
for Global Variable(BF, 0, 255, 1);
    Modify Global Variable(BE, Append To Array, BF);
    Global.BD = Global.BE[BF]
    #wait for .1 seconds
    """
    



"""
[[0, 20, 0], [0, 20, 3], [0, 20, 3.5], [0, 20, 6.5],[0, 20, 7], [0, 20, 10],
[0, 17, 0], [0, 17, 3],[0, 17, 3.5], [0, 17, 6.5], [0, 17, 7], [0, 17, 10],
 [0, 16.5, 0], [0, 16.5, 3], [0, 16.5, 3.5], [0, 16.5, 6.5], [0, 16.5, 7], [0, 16.5, 10],
 [0, 13.5, 0], [0, 13.5, 3], [0, 13.5, 3.5], [0, 13.5, 6.5], [0, 13.5, 7], [0, 13.5, 10],
 [0, 13, 0], [0, 13, 3], [0, 13, 3.5], [0, 13, 6.5], [0, 13, 7], [0, 13, 10],
 [0, 10, 0], [0, 10, 3], [0, 10, 3.5], [0, 10, 6.5], [0, 10, 7], [0, 10, 10]]

"""
##########################################################################################################################
def mod_sides(face, face_shift):
        # for the other faces:
    # Down face:
    findex=1;
    face_num=1;
    for i in range(0,12,1):
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=face_shift; # move to next face and its 4 vectors
##########################################################################################################################    
# find the differences for the front turn?
# front turn rule
def mod_front_turn(face, face_num):
    #  vector destination - vector start
    # print "modify glob"
    findex = 1;

    # for the white face
    for i in range(0,32,1):
        if ( face_num == 5 ): face_num = 6;
        print("Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global."+face+ str(face_num) + "[" + str(findex) + "]));");
        findex+=1;
        if (findex > 4 ): # bigger than 4, reset back to 1
            findex=1; # reset the vectors, 1-4
            face_num +=1; # move to next face and its 4 vectors        
  
    # for the other faces:
    # Down face:
    mod_sides("Down_", 1);

    # Left face:
    mod_sides("Left_", 3);

    # Up face:
    mod_sides("Up_", 1);

    # Right face:
    mod_sides("Right_", 3);
##########################################################################################################################
    #def print_vector(vector):
        
##########################################################################################################################
### FOR CLOCKWISE - DEFAULT NOTATION - NOT INVERSE(inverse should switch start and end?)
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
        difference[i] = vector_face_end[i] - vector_face_start[i]


# this is where i could loop the additions ( well encapsulating this whole statement)
    #print first white 9 tiles first
    return "Vector(" + str(difference[0])+ ", " + str(difference[1])+ ",  " + str(difference[2]) + ");";
##    return "Vector(" + str(difference[0]/4)+ ", " + str(difference[1]/4)+ ",  " + str(difference[2]/4) + ");";

    # then print the rest of the associated faces?

##########################################################################################################################
def glob_coords(index):
    # print  initial part, index from 1-84?
    return"Global.fake_coords[Global.position_index["+str(index)+"]] += ";

    
##########################################################################################################################
# for the front facing side of a turn. given white face -> front turn, given red -> right turn, given green -> down turn
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

##########################################################################################################################
def calc_red_side():
    # for the

##########################################################################################################################
def calc_orange_side():

##########################################################################################################################
def calc_green_side():

##########################################################################################################################
def calc_blue_side():

##########################################################################################################################
def calc_black_side():

##########################################################################################################################
def calc_white_side():

##########################################################################################################################
#mod_front_turn("Front_", 1);

white_vector =  [[],[0, 20, 0], [0, 20, 3], [0, 17, 3], [0, 17, 0], [0, 20, 3.5], [0, 20, 6.5], [0, 17, 6.5], [0, 17, 3.5], [0, 20, 7], [0, 20, 10], [0, 17, 10], [0, 17, 7], [0, 16.5, 0], [0, 16.5, 3], [0, 13.5, 3], [0, 13.5, 0], [0, 16.5, 3.5], [0, 16.5, 6.5], [0, 13.5, 6.5], [0, 13.5, 3.5], [0, 16.5, 7], [0, 16.5, 10], [0, 13.5, 10], [0, 13.5, 7], [0, 13, 0], [0, 13, 3], [0, 10, 3], [0, 10, 0], [0, 13, 3.5], [0, 13, 6.5], [0, 10, 6.5], [0, 10, 3.5], [0, 13, 7], [0, 13, 10], [0, 10, 10], [0, 10, 7]]
green_vector = [[],[0, 10, 0], [0, 10, 3], [3, 10, 3], [3, 10, 0], [0, 10, 3.5], [0, 10, 6.5], [3, 10, 6.5], [3, 10, 3.5], [0, 10, 7], [0, 10, 10], [3, 10, 10], [3, 10, 7], [3.5, 10, 0], [3.5, 10, 3], [6.5, 10, 3], [6.5, 10, 0], [3.5, 10, 3.5], [3.5, 10, 6.5], [6.5, 10, 6.5], [6.5, 10, 3.5], [3.5, 10, 7], [3.5, 10, 10], [6.5, 10, 10], [6.5, 10, 7], [7, 10, 0], [7, 10, 3], [10, 10, 3], [10, 10, 0], [7, 10, 3.5], [7, 10, 6.5], [10, 10, 6.5], [10, 10, 3.5], [7, 10, 7], [7, 10, 10], [10, 10, 10], [10, 10, 7]]
orange_vector = [[],[10, 20, 0], [7, 20, 0], [7, 17, 0], [10, 17, 0], [6.5, 20, 0], [3.5, 20, 0], [3.5, 17, 0], [6.5, 17, 0], [3, 20, 0], [0, 20, 0], [0, 17, 0], [3, 17, 0], [10, 16.5, 0], [7, 16.5, 0], [7, 13.5, 0], [10, 13.5, 0], [6.5, 16.5, 0], [3.5, 16.5, 0], [3.5, 13.5, 0], [6.5, 13.5, 0], [3, 16.5, 0], [0, 16.5, 0], [0, 13.5, 0], [3, 13.5, 0], [10, 13, 0], [7, 13, 0], [7, 10, 0], [10, 10, 0], [6.5, 13, 0], [3.5, 13, 0], [3.5, 10, 0], [6.5, 10, 0], [3, 13, 0], [0, 13, 0], [0, 10, 0], [3, 10, 0]]

red_vector =  [[],[0, 20, 10], [3, 20, 10], [3, 17, 10], [0, 17, 10], [3.5, 20, 10], [6.5, 20, 10], [6.5, 17, 10], [3.5, 17, 10], [7, 20, 10], [10, 20, 10], [10, 17, 10], [7, 17, 10], [0, 16.5, 10], [3, 16.5, 10], [3, 13.5, 10], [0, 13.5, 10], [3.5, 16.5, 10], [6.5, 16.5, 10], [6.5, 13.5, 10], [3.5, 13.5, 10], [7, 16.5, 10], [10, 16.5, 10], [10, 13.5, 10], [7, 13.5, 10], [0, 13, 10], [3, 13, 10], [3, 10, 10], [0, 10, 10], [3.5, 13, 10], [6.5, 13, 10], [6.5, 10, 10], [3.5, 10, 10], [7, 13, 10], [10, 13, 10], [10, 10, 10], [7, 10, 10]]
blue_vector = [[],[10, 20, 0], [10, 20, 3], [7, 20, 3], [7, 20, 0], [10, 20, 3.5], [10, 20, 6.5], [7, 20, 6.5], [7, 20, 3.5], [10, 20, 7], [10, 20, 10], [7, 20, 10], [7, 20, 7], [6.5, 20, 0], [6.5, 20, 3], [3.5, 20, 3], [3.5, 20, 0], [6.5, 20, 3.5], [6.5, 20, 6.5], [3.5, 20, 6.5], [3.5, 20, 3.5], [6.5, 20, 7], [6.5, 20, 10], [3.5, 20, 10], [3.5, 20, 7], [3, 20, 0], [3, 20, 3], [0, 20, 3], [0, 20, 0], [3, 20, 3.5], [3, 20, 6.5], [0, 20, 6.5], [0, 20, 3.5], [3, 20, 7], [3, 20, 10], [0, 20, 10], [0, 20, 7]]
black_vector = [[],[10, 20, 10], [10, 20, 7], [10, 17, 7], [10, 17, 10], [10, 20, 6.5], [10, 20, 3.5], [10, 17, 3.5], [10, 17, 6.5], [10, 20, 3], [10, 20, 0], [10, 17, 0], [10, 17, 3], [10, 16.5, 10], [10, 16.5, 7], [10, 13.5, 7], [10, 13.5, 10], [10, 16.5, 6.5], [10, 16.5, 3.5], [10, 13.5, 3.5], [10, 13.5, 6.5], [10, 16.5, 3], [10, 16.5, 0], [10, 13.5, 0], [10, 13.5, 3], [10, 13, 10], [10, 13, 7], [10, 10, 7], [10, 10, 10], [10, 13, 6.5], [10, 13, 3.5], [10, 10, 3.5], [10, 10, 6.5], [10, 13, 3], [10, 13, 0], [10, 10, 0], [10, 10, 3]]


# would have to type out 84 of these.. yikes.. need to reconsider the ordering? maybe store the array by face.. every 4 is another face.. its at least more mathy
# F1 - 1 and F3 - 2
#vector_difference(white_vector[1], white vector[3]); # + 4?
## + 4?
##########################################################################################################################
def main():
    # modify the position array first for the front turn?
    mod_front_turn("Front_", 1);

    # continue with calculations now, using position index as done in the past.
    position_index=0
    # white face - front turn
#    for i in range():
# keep track of position index?
    position_index = calc_facing_side(white_vector, position_index);
    #calc_facing_side(white_vector, position_index);
    #mod_front_turn("Front_", 1);


    #print(position_index);
        
    #a = vector_difference(white_vector[1], white vector[3])
   # print( glob_coords(position_index) + vector_difference(white_vector[1], white_vector[10]) );


    # other faces?

if __name__ == "__main__":
    main();
    


## crap


    
            ##        position_index+=1; # next point
##        print( glob_coords(position_index) + vector_difference(F1[posA], F3[posB]));
##        position_index+=1; # next point
##        posA+=1; # go 2->3
##        posB+=1; # go 3->4
##        print( glob_coords(position_index) + vector_difference(F1[posA], F3[posB]));
##        position_index+=1; # next point
##        posA+=1; # go 3->4
##        if ( posB >=5):
##            posB=1; # 4->1
##        print( glob_coords(position_index) + vector_difference(F1[posA], F3[posB]));
##        print( glob_coords(position_index) + vector_difference(F7[posA], F1[posB]));
##        position_index+=1; # next point
##        print( glob_coords(position_index) + vector_difference(F2[posA], F6[posB]));
##        position_index+=1; # next point
##        print( glob_coords(position_index) + vector_difference(F6[posA], F8[posB]));
##        position_index+=1; # next point
##        print( glob_coords(position_index) + vector_difference(F8[posA], F4[posB]));
##        position_index+=1; # next point
##        print( glob_coords(position_index) + vector_difference(F4[posA], F2[posB]));                 

##        posA+=1; # go 1->2->3->4
##        posB+=1; # go 2->3->4->1
##
##        if (posA >=4):
##            posB=1; # when position start is 4, make position end 1
