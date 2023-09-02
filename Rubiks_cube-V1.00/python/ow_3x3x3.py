""" add file integration, output to text file
TODO
- create function for each face - each face has certain vectors, and color
  other wise will print same template: Create Beam() functions
- figure out math for each tile or cubie to move to its correct position

DESC: script to write rubiks cube in Overwatch
first create the solved cube - requires function for each face
each face requires 9 tiles
each tile should have an array of 4 locations - 1,2,3,4 - anchors for creating beams
each face will have certain logic to move each of its 24 pieces
        (9 for front + 5*3 for other faces


6x6 array to hold each values for each. there is one constant.
x = constant, y [i][], z = [][k]
vector = (0, y[i][], z[][k])
i++ # go to next y value, etc.
goes through all 6 row by row down all the columns. 


"""


# TODO
# - fix up bot positions
# - maybe  change camera angle? press button to change, to each face?
# - maybe add inverse? ( prob not, just leave as x3 moves)
# - think about hud and stuff


from enum import Enum
# create 54  variables for each of the 54 spaces for 6 sides - 
class cubie:
    def __init__(self):
        p='a';
    # add 4 beams
    # add vector spacing


class Side(Enum):
    FRONT = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    UP = 4
    BACK = 5 
    
    
##########################################################################################################################
def variables_set():
    print("variables\n{\n\tglobal:");
    num = 1
    face = Side.FRONT;
    for index in range(0,54):
        if (face == Side.FRONT):
            print("\t\t"+ str(index) + ": Front_" + str(num) );
            num=num+1;
        elif (face == Side.LEFT):
            print("\t\t"+ str(index) + ": Left_" + str(num) );            
            num=num+1;
        elif (face == Side.DOWN):
            print("\t\t"+ str(index) + ": Down_" + str(num) );            
            num=num+1;
        elif (face == Side.RIGHT):
            print("\t\t"+ str(index) + ": Right_" + str(num) );            
            num=num+1;
        elif (face == Side.UP):
            print("\t\t"+ str(index) + ": Up_" + str(num) );            
            num=num+1;
        elif (face == Side.BACK):
            print("\t\t"+ str(index) + ": Back_" + str(num) );            
            num=num+1;
        if (index == 53):
            print("}");
            return;

        if (num%10 == 0):
            face = Side(face.value + 1); # go to next face every 9 squares
            num=1; # reset to start over for each face


##########################################################################################################################
def global_set():
    print("actions\n{\n\t");
    num = 1;
    face = Side.FRONT;
    
    for i in range(0,216,1):
        print("initialize sequence "+ face.value +" positions");
        print("Global.", end ="");
        print("temp" + str(num) + " = Vector(" + str(_x) + ", " + str(_y) + ", "+ str(_z) + ")");

        
        # set the global vars to the start. ( need to now get the vector values here, or something)
##        if (face == Side.FRONT):
##            set_global("Front_", front_vector);
            

def set_global(side, _x, _y, _z):
    print(side + str(num) + " = Vector(" + str(_x) + ", " + str(_y) + ", "+ str(_z) + ")" );
    
##########################################################################################################################    
### OLD CRAP             
##########################################################################################################################    
# need capital colors
# vector needs to be correct
# if i fill it correctly, just need to match this face with the vectors of the white board
def OLD_Create_Beam( _color, _vector_start, _vector_end):
    print("Create Beam Effect(All Players(All Teams), Good Beam, Vector(" + str(_vector_start[0]) + ", " + str(_vector_start[1]) + ", "+ str(_vector_start[2]) + "), Vector(" + str(_vector_end[0]) + ", " + str(_vector_end[1]) + ", " + str(_vector_end[2]) + "), Color(" + str(_color) + "), Visible To Position and Radius);");

##########################################################################################################################
def old_create_beams(__color,  _face_vector):
    # print(face_vector);
    # to create the beams, need to create white 1, then white 2, then white 3.. how to do this now
    # create white face 1

    """
    Modify Global Variable(Front_1, Append To Array, Vector(0, 0, 0));

     Create Beam Effect(All Players(All Teams), Good Beam, Global.Front_1[0], Global.Front_1[1],
     Color(White), Visible To Position and Radius);
    """
    face_num = 1;
    i = 0;
    while ( i < 36):  
        print("\"" + __color + " " + str(face_num) + "\"");
        # beam 1
        Create_Beam(__color,  _face_vector[i], _face_vector[i+1]);
        #beam 2
        Create_Beam(__color,  _face_vector[i], _face_vector[i+6]);    
        #beam 3
        Create_Beam(__color,  _face_vector[i+7], _face_vector[i+1]);
        #beam4
        Create_Beam(__color,  _face_vector[i+7], _face_vector[i+6]);
        if (face_num % 3 == 0):
            i+=6; # skip to next row of 4
        face_num+=1;
        i+=2;
        
        if (face_num >=10): break;

##########################################################################################################################
### NEW CRAP

        ## face1-4 will = i+1, 1+etc
        # do the switching here, to pass 1-4 for each face, adding to the cube coords by face values instead of row and columns

        
def create_vector(_color, const,  col, row):
    # initialize
    face_vector = [[] for i in range(36)]; # create list of 36 lists
    c_count = 0;
    r_count = 0;
    
    # now go through each, and append to 2D list
    for index in range(0,36,1):
        if (_color == "White" or _color == "Black"):
            face_vector[index].append(const);
            face_vector[index].append(col[c_count]);
            face_vector[index].append(row[r_count]);
            r_count+=1;
            # every 6 rows go to next column
            if (r_count % 6  == 0 ):
                c_count+=1; # go to next column every 6
                r_count=0; # reset row counter for next column

        if (_color == "Green" or _color == "Blue"):
                face_vector[index].append(col[c_count]);
                face_vector[index].append(const);
                face_vector[index].append(row[r_count]);
                r_count+=1;
                # every 6 rows go to next column
                if (r_count % 6  == 0 ):
                    c_count+=1; # go to next column every 6
                    r_count=0; # reset row counter for next column

        if (_color == "Orange" or _color == "Red"):                          
                face_vector[index].append(row[r_count]);
                face_vector[index].append(col[c_count]);     
                face_vector[index].append(const);
                r_count+=1;
                # every 6 rows go to next column
                if (r_count % 6  == 0 ):
                    c_count+=1; # go to next column every 6
                    r_count=0; # reset row counter for next column

    return face_vector
        
    #create_beams(_color, face_vector);

# attempt 2 at scripting a rubik's cube in ow workshop
"""
Modify Global Variable(Front_1, Append To Array, Vector(0, 0, 0));
Create Beam Effect(All Players(All Teams), Good Beam, Global.Front_1[0], Global.Front_1[1],
Color(White), Visible To Position and Radius);
"""
##########################################################################################################################
def modify_constants(face, v):
    # print("Global."+face+" = Vector("+ str(v[0]) + ", " + str(v[1]) + ", "+ str(v[2]) + "));");
    # print("Modify Global Variable(" + face +", Append To Array, Vector(" + str(v[0]) + ", " + str(v[1]) + ", "+ str(v[2]) + "));");
    # append the constants to their respective array
    print("Modify Global Variable(" + face +", Append To Array, Vector(" + str(v[0]) + ", " + str(v[1]) + ", "+ str(v[2]) + "));");
   

##########################################################################################################################
def modify_cube(const_v,index):
    # then append to cube coords array
    print("Modify Global Variable(Cube_coords, Append To Array, Global." + str(const_v) + "[" + str(index)+ "]);");
    
##########################################################################################################################
# pass in the variable name {Front_1}, array location?
##def Create_Beam( _color, start, end, face):    
##    #print("Create Beam Effect(All Players(All Teams), Good Beam, Vector(" + str(_vector_start[0]) + ", " + str(_vector_start[1]) + ", "+ str(_vector_start[2]) + "), Vector(" + str(_vector_end[0]) + ", " + str(_vector_end[1]) + ", " + str(_vector_end[2]) + "), Color(" + str(_color) + "), Visible To Position and Radius);");
##    print("Create Beam Effect(All Players(All Teams), Good Beam, Global."+ face + "["+ str(start)+ "], Global."+ face +"["+ str(end) +"], Color("+ _color+"), Visible To Position and Radius);");
def Create_Beams( _color, start, end,):    
    print("Create Beam Effect(All Players(All Teams), Good Beam, Global.Cube_coords["+ str(start)+ "], Global.Cube_coords["+ str(end) +"], Color("+ _color+"), Visible To Position and Radius);");

##########################################################################################################################
def create_face(color, face, index, face_vector):
    # call this once for each color/face , white calls this one time? pass in (color, face, face_vector)
    # 9 for each square for one face - so like white face
    face_num = 1;
    i = 0;
    while ( i < 36):
        # index=index * face_num;
        print("\""+ color +" "+ str(face_num)+"\""); # color tile, for initializiation comment
        temp_face =  face + str(face_num); # face_1-9
        # need four vectors per face square
        modify_constants( temp_face, face_vector[i]); # modify the first vector - v1 for F1
        modify_constants( temp_face, face_vector[i+1]); # modify the first vector - v2 for F1
        modify_constants( temp_face, face_vector[i+2]); # modify the first vector - v4 for F1
        modify_constants( temp_face, face_vector[i+3]); # modify the first vector - v3 for F1
    # append  the constants to the cube coords array now. this will hold all 216 values.. or so.
        print("\""+str(face_num)+" sequence started\"");
        modify_cube(temp_face, 1);
        modify_cube(temp_face, 2);
        modify_cube(temp_face, 3);
        modify_cube(temp_face, 4);


        # maybe first create the whole array in above loop
        # then create loop to create beams from 0-216
        # now this is where i need to have an index from 0-216 to create the beams with the cub_coords vector
        # dont use the constants like i am here
       #send in the array Cube[1] - Cube[216]
        Create_Beams(color,  index+1, index+2, );
        Create_Beams(color,  index+1, index+4, );
        Create_Beams(color,  index+3, index+2, );
        Create_Beams(color,  index+3, index+4,);
        index+=4; # increase by four for next go        

     
            
        face_num+=1;
        i+=4;
        if (face_num >=10): break;

    return index; # return back to main to be passed and continued by another color?


##########################################################################################################################
### FRONT WHITE FACE
    
def white_front(findex):    
    color = str("White");
    face = "Front_";
    
    const = -0.1; # should be x value of 0, on the x plane @ 0 - front face
    
    #initial starting point top left corner
    row = [0, 3, 3.5, 6.5, 7, 10]; # z values
    col = [20, 17, 16.5, 13.5, 13, 10]; # y values

    white_vector = print_vector(color, const, col, row);
    print("\nwhite  " , white_vector);
    print("\n");

    # color, face
    return create_face(color, face, findex, white_vector);

    # can now use white face vector to do some maths

#def front(front_vector):
    # given the vector, find the faces that need to be changed.
    # in this case this should swap around all 9 white tiles, and the other 15 tiles
    

##########################################################################################################################
### BACK BLACK/YELLOW FACE
    
def black_back(findex):    
    color = str("Black");       
    face = "Back_";
    const = 10.1; # should be x value of 10, on the x plane @ 10 - back face
    
    #initial starting point top left corner
    #row = [0, 3, 3.5, 6.5, 7, 10]; # z values
    row = [10, 7, 6.5, 3.5, 3, 0]; # z values
    col = [20, 17, 16.5, 13.5, 13, 10]; # y values


    black_vector = print_vector(color, const, col, row);
    print("\nblack  "  ,black_vector);
    print("\n");

    return create_face(color, face, findex, black_vector);

    # can now use white face vector to do some maths
##########################################################################################################################
### LEFT ORANGE FACE

def orange_left(findex):
    color = str("Orange");
    face = "Left_";

    const = -0.01 ; # should be z value of 0 on z plane - the left face

# need to change these values, a slight difference. these are the corner pieces.
    #row = [0, 3, 3.5, 6.5, 7, 10]; # x values
    row = [10, 7, 6.5, 3.5, 3, 0]; # x values
    col = [20, 17, 16.5, 13.5, 13, 10]; # y values


    orange_vector = print_vector(color, const, col, row);
    print("\norange  "  ,orange_vector);
    print("\n");

    return create_face(color,face, findex, orange_vector);
    
##########################################################################################################################
### RIGHT RED FACE

def right_red(findex):
    color = str("Red");
    face = "Right_";

    const = 10.09 ; # should be z value of 10 on z plane- the right face

    row = [0, 3, 3.5, 6.5, 7, 10]; # x values
    col = [20, 17, 16.5, 13.5, 13, 10]; # y values

    red_vector = print_vector(color, const, col, row);
    print("\nred  "  ,red_vector);
    print("\n");

    return create_face(color, face, findex, red_vector);

##########################################################################################################################
### DOWN GREEN FACE

def green_down(findex):
    color = str("Green");
    face = "Down_";

    const = 9.9; # should be y value of 10 on y plane - the bottom face
    row = [0, 3, 3.5, 6.5, 7, 10]; # z values
    col = [0, 3, 3.5, 6.5, 7, 10]; # x values

    green_vector = print_vector(color, const, col, row);
    print("\ngreen  "  ,green_vector);
    print("\n");

    return create_face(color, face, findex, green_vector);

    # can now use green face vector for maths
##########################################################################################################################
### UP BLUE FACE

def blue_up(findex):
    color = str("Blue");
    face = "Up_";

    const = 20.1; # should be y value of 20 on y plane - the top face
    row = [0, 3, 3.5, 6.5, 7, 10]; # z values
    col = [10, 7, 6.5, 3.5, 3, 0]; # x values


    blue_vector = print_vector(color, const, col, row);
    print("\nblue  "  , blue_vector);
    print("\n");

    return create_face(color, face, findex, blue_vector);

    # can now use green face vector for maths
        
##    Create_Beam(color,  white_vector[0], white_vector[1]);
##    Create_Beam(color,  white_vector[7], white_vector[1]);
##    Create_Beam(color,  white_vector[0], white_vector[6]);
##    Create_Beam(color,  white_vector[7], white_vector[



##########################################################################################################################       
# printing vectors
def print_vector(_color, const,  col, row):
    # initialize
    face_vector = [[] for i in range(36)]; # create list of 36 lists
    c_count = 0;
    r_count = 0;
    i = 0
    # now go through each, and append to 2D list
    for index in range(0,36,4):
        if (_color == "White" or _color == "Black"):
            #1 - 0,0
            face_vector[index].append(const);
            face_vector[index].append(col[c_count]);
            face_vector[index].append(row[r_count]);
            #2 - 0,1
            face_vector[index+1].append(const);
            face_vector[index+1].append(col[c_count]);
            face_vector[index+1].append(row[r_count+1]);
            #3 - 1,1
            face_vector[index+2].append(const);
            face_vector[index+2].append(col[c_count+1]);
            face_vector[index+2].append(row[r_count+1]);
            #4 - 1,0
            face_vector[index+3].append(const);
            face_vector[index+3].append(col[c_count+1]);
            face_vector[index+3].append(row[r_count]);
           

            r_count +=2;
           #c_count+=2;
            if (r_count % 6 ==  0): # or r_count == 16 ):
                r_count= 0;
                c_count+=2; # go to next row and column

        if (_color == "Green" or _color == "Blue"):
            #1 - 0,0
            face_vector[index].append(col[c_count]);
            face_vector[index].append(const);
            face_vector[index].append(row[r_count]);
            #2 - 0,1
            face_vector[index+1].append(col[c_count]);
            face_vector[index+1].append(const);
            face_vector[index+1].append(row[r_count+1]);
            #3 - 1,1
            face_vector[index+2].append(col[c_count+1]);
            face_vector[index+2].append(const);
            face_vector[index+2].append(row[r_count+1]);
            #4 - 1,0
            face_vector[index+3].append(col[c_count+1]);
            face_vector[index+3].append(const);
            face_vector[index+3].append(row[r_count]);
           

            r_count +=2;
           #c_count+=2;
            if (r_count % 6 ==  0): # or r_count == 16 ):
                r_count= 0;
                c_count+=2; # go to next row and column

        if (_color == "Orange" or _color == "Red"):                          
            #1 - 0,0
            face_vector[index].append(row[r_count]);
            face_vector[index].append(col[c_count]);     
            face_vector[index].append(const);
            #2 - 0,1
            face_vector[index+1].append(row[r_count+1]);
            face_vector[index+1].append(col[c_count]);     
            face_vector[index+1].append(const);
            #3 - 1,1
            face_vector[index+2].append(row[r_count+1]);
            face_vector[index+2].append(col[c_count+1]);     
            face_vector[index+2].append(const);
            #4 - 1,0
            face_vector[index+3].append(row[r_count]);
            face_vector[index+3].append(col[c_count+1]);     
            face_vector[index+3].append(const);
           

            r_count +=2;
           #c_count+=2;
            if (r_count % 6 ==  0): # or r_count == 16 ):
                r_count= 0;
                c_count+=2; # go to next row and column

    return face_vector
##########################################################################################################################
def main():
    #tetsing
    #v = [0,1,2,3,4,5]
    #Create_Beam("Green", v);

    # creating all the variables
    # variables_set();
    face_index = 0

##    mcolor = "White"
##    mconst = 0 
##  #initial starting point top left corner
##    mrow = [0, 3, 3.5, 6.5, 7, 10]; # z values
##    mcol = [20, 17, 16.5, 13.5, 13, 10]; # y values

    
    #print(print_vector(mcolor, mconst, mcol, mrow));

    
    # create some beams, like the white face 
    #print("\""+ comment + "\""); # should print out "comment here":

##    white_front(face_index);
##    green_down(face_index);
##    orange_left(face_index);    
##    right_red(face_index);
##    blue_up(face_index);
##    black_back(face_index);

    
##    
##    face_index = white_front(face_index);
##    face_index = green_down(face_index);
##    face_index = orange_left(face_index);
    face_index = 108
    face_index = right_red(face_index);
    face_index = blue_up(face_index);
    face_index = black_back(face_index);


##########################################################################################################################
if __name__ == '__main__':
    #sys.exit( main() );
    main();
