# attempt 2 at scripting a rubik's cube in ow workshop

"""
Modify Global Variable(Front_1, Append To Array, Vector(0, 0, 0));
Create Beam Effect(All Players(All Teams), Good Beam, Global.Front_1[0], Global.Front_1[1],
Color(White), Visible To Position and Radius);
"""



def modify(face, v):
    print("Modify Global Variable(" + face +", Append To Array, Vector(" + str(v[0]) + ", " + str(v[1]) + ", "+ str(v[2]) + ");");


# pass in the variable name {Front_1}, array location?
def Create_Beam( _color, start, end, face):
    #print("Create Beam Effect(All Players(All Teams), Good Beam, Vector(" + str(_vector_start[0]) + ", " + str(_vector_start[1]) + ", "+ str(_vector_start[2]) + "), Vector(" + str(_vector_end[0]) + ", " + str(_vector_end[1]) + ", " + str(_vector_end[2]) + "), Color(" + str(_color) + "), Visible To Position and Radius);");
    print("Create Beam Effect(All Players(All Teams), Good Beam, Global."+ face + "["+ str(start)+ "], Global."+ face +"["+ str(end) +"], \
    Color("+ _color+"), Visible To Position and Radius);");



# coordinate 1 for F1
init_face = "Front_1";
face = "Front_";
face_vector =[[0, 20, 0], [0, 20, 3], [0, 20, 3.5], [0, 20, 6.5], [0, 20, 7], [0, 20, 10], [0, 17, 0], [0, 17, 3], [0, 17, 3.5], [0, 17, 6.5], [0, 17, 7], [0, 17, 10], [0, 16.5, 0], [0, 16.5, 3], [0, 16.5, 3.5], [0, 16.5, 6.5], [0, 16.5, 7], [0, 16.5, 10], [0, 13.5, 0], [0, 13.5, 3], [0, 13.5, 3.5], [0, 13.5, 6.5], [0, 13.5, 7], [0, 13.5, 10], [0, 13, 0], [0, 13, 3], [0, 13, 3.5], [0, 13, 6.5], [0, 13, 7], [0, 13, 10], [0, 10, 0], [0, 10, 3], [0, 10, 3.5], [0, 10, 6.5], [0, 10, 7], [0, 10, 10]]
color = "White";

# call this once for each color/face , white calls this one time? pass in (color, face, face_vector)
# 9 for each square for one face - so like white face
face_num = 1;
i = 0;
while ( i < 36):
    print("\""+ color +""+ str(face_num)+"\""); # color tile, for initializiation comment
    temp_face =  face + str(face_num); # face_1-9
    # need four vectors per face square
    modify(temp_face, face_vector[i]); # modify the first vector - v1 for F1
    modify(temp_face, face_vector[i+1]); # modify the first vector - v2 for F1
    modify(temp_face, face_vector[i+7]); # modify the first vector - v4 for F1
    modify(temp_face, face_vector[i+6]); # modify the first vector - v3 for F1
   
    Create_Beam(color,  i, i+1, temp_face);
    Create_Beam(color,  i, i+6, temp_face);
    Create_Beam(color,  i+7, i+1, temp_face);
    Create_Beam(color,  i+7, i+6, temp_face);

    if (face_num % 3 == 0):
        i+=6; # skip to next row of 4
        
    face_num+=1;
    i+=2;

    if (face_num >=10): break;


    

