subroutines
{
	2: Down
}
rule("Down turn - subroutine with animation")
{
	event
	{
		Subroutine;
		Down;
	}

	actions
	{
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_1[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_1[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_1[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_1[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_2[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_2[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_2[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_2[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_3[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_3[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_3[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_3[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_4[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_4[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_4[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_4[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_5[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_5[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_5[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_5[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_6[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_6[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_6[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_6[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_7[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_7[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_7[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_7[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_8[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_8[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_8[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_8[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_9[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_9[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_9[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Down_9[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_7[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_7[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_7[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_7[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_8[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_8[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_8[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_8[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_9[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_9[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_9[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Front_9[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_7[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_7[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_7[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_7[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_8[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_8[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_8[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_8[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_9[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_9[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_9[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Right_9[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_7[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_7[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_7[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_7[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_8[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_8[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_8[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_8[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_9[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_9[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_9[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Back_9[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_7[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_7[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_7[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_7[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_8[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_8[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_8[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_8[4]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_9[1]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_9[2]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_9[3]));
Modify Global Variable(position_index, Append To Array, Index Of Array Value(Global.Cube_coords, Global.Left_9[4]));
For Global Variable(turn_counter, 0, 4, 1);
Global.Cube_coords[Global.position_index[1]] += Vector(0.0, 0.0,  2.5);
Global.Cube_coords[Global.position_index[2]] += Vector(0.75, 0.0,  1.75);
Global.Cube_coords[Global.position_index[3]] += Vector(0.0, 0.0,  1.0);
Global.Cube_coords[Global.position_index[4]] += Vector(-0.75, 0.0,  1.75);
Global.Cube_coords[Global.position_index[5]] += Vector(0.875, 0.0,  1.625);
Global.Cube_coords[Global.position_index[6]] += Vector(1.625, 0.0,  0.875);
Global.Cube_coords[Global.position_index[7]] += Vector(0.875, 0.0,  0.125);
Global.Cube_coords[Global.position_index[8]] += Vector(0.125, 0.0,  0.875);
Global.Cube_coords[Global.position_index[9]] += Vector(1.75, 0.0,  0.75);
Global.Cube_coords[Global.position_index[10]] += Vector(2.5, 0.0,  0.0);
Global.Cube_coords[Global.position_index[11]] += Vector(1.75, 0.0,  -0.75);
Global.Cube_coords[Global.position_index[12]] += Vector(1.0, 0.0,  0.0);
Global.Cube_coords[Global.position_index[13]] += Vector(-0.875, 0.0,  1.625);
Global.Cube_coords[Global.position_index[14]] += Vector(-0.125, 0.0,  0.875);
Global.Cube_coords[Global.position_index[15]] += Vector(-0.875, 0.0,  0.125);
Global.Cube_coords[Global.position_index[16]] += Vector(-1.625, 0.0,  0.875);
Global.Cube_coords[Global.position_index[17]] += Vector(0.0, 0.0,  0.75);
Global.Cube_coords[Global.position_index[18]] += Vector(0.75, 0.0,  0.0);
Global.Cube_coords[Global.position_index[19]] += Vector(0.0, 0.0,  -0.75);
Global.Cube_coords[Global.position_index[20]] += Vector(-0.75, 0.0,  0.0);
Global.Cube_coords[Global.position_index[21]] += Vector(0.875, 0.0,  -0.125);
Global.Cube_coords[Global.position_index[22]] += Vector(1.625, 0.0,  -0.875);
Global.Cube_coords[Global.position_index[23]] += Vector(0.875, 0.0,  -1.625);
Global.Cube_coords[Global.position_index[24]] += Vector(0.125, 0.0,  -0.875);
Global.Cube_coords[Global.position_index[25]] += Vector(-1.75, 0.0,  0.75);
Global.Cube_coords[Global.position_index[26]] += Vector(-1.0, 0.0,  0.0);
Global.Cube_coords[Global.position_index[27]] += Vector(-1.75, 0.0,  -0.75);
Global.Cube_coords[Global.position_index[28]] += Vector(-2.5, 0.0,  0.0);
Global.Cube_coords[Global.position_index[29]] += Vector(-0.875, 0.0,  -0.125);
Global.Cube_coords[Global.position_index[30]] += Vector(-0.125, 0.0,  -0.875);
Global.Cube_coords[Global.position_index[31]] += Vector(-0.875, 0.0,  -1.625);
Global.Cube_coords[Global.position_index[32]] += Vector(-1.625, 0.0,  -0.875);
Global.Cube_coords[Global.position_index[33]] += Vector(0.0, 0.0,  -1.0);
Global.Cube_coords[Global.position_index[34]] += Vector(0.75, 0.0,  -1.75);
Global.Cube_coords[Global.position_index[35]] += Vector(0.0, 0.0,  -2.5);
Global.Cube_coords[Global.position_index[36]] += Vector(-0.75, 0.0,  -1.75);
Global.Cube_coords[Global.position_index[37]] += Vector(0.025, 0.0,  2.5225);
Global.Cube_coords[Global.position_index[38]] += Vector(0.775, 0.0,  1.7725);
Global.Cube_coords[Global.position_index[39]] += Vector(0.775, 0.0,  1.7725);
Global.Cube_coords[Global.position_index[40]] += Vector(0.025, 0.0,  2.5225);
Global.Cube_coords[Global.position_index[41]] += Vector(0.9, 0.0,  1.6475);
Global.Cube_coords[Global.position_index[42]] += Vector(1.65, 0.0,  0.8975);
Global.Cube_coords[Global.position_index[43]] += Vector(1.65, 0.0,  0.8975);
Global.Cube_coords[Global.position_index[44]] += Vector(0.9, 0.0,  1.6475);
Global.Cube_coords[Global.position_index[45]] += Vector(1.775, 0.0,  0.7725);
Global.Cube_coords[Global.position_index[46]] += Vector(2.525, 0.0,  0.0225);
Global.Cube_coords[Global.position_index[47]] += Vector(2.525, 0.0,  0.0225);
Global.Cube_coords[Global.position_index[48]] += Vector(1.775, 0.0,  0.7725);
Global.Cube_coords[Global.position_index[49]] += Vector(2.525, 0.0,  -0.0225);
Global.Cube_coords[Global.position_index[50]] += Vector(1.775, 0.0,  -0.7725);
Global.Cube_coords[Global.position_index[51]] += Vector(1.775, 0.0,  -0.7725);
Global.Cube_coords[Global.position_index[52]] += Vector(2.525, 0.0,  -0.0225);
Global.Cube_coords[Global.position_index[53]] += Vector(1.65, 0.0,  -0.8975);
Global.Cube_coords[Global.position_index[54]] += Vector(0.9, 0.0,  -1.6475);
Global.Cube_coords[Global.position_index[55]] += Vector(0.9, 0.0,  -1.6475);
Global.Cube_coords[Global.position_index[56]] += Vector(1.65, 0.0,  -0.8975);
Global.Cube_coords[Global.position_index[57]] += Vector(0.775, 0.0,  -1.7725);
Global.Cube_coords[Global.position_index[58]] += Vector(0.025, 0.0,  -2.5225);
Global.Cube_coords[Global.position_index[59]] += Vector(0.025, 0.0,  -2.5225);
Global.Cube_coords[Global.position_index[60]] += Vector(0.775, 0.0,  -1.7725);
Global.Cube_coords[Global.position_index[61]] += Vector(-0.025, 0.0,  -2.5025);
Global.Cube_coords[Global.position_index[62]] += Vector(-0.775, 0.0,  -1.7525);
Global.Cube_coords[Global.position_index[63]] += Vector(-0.775, 0.0,  -1.7525);
Global.Cube_coords[Global.position_index[64]] += Vector(-0.025, 0.0,  -2.5025);
Global.Cube_coords[Global.position_index[65]] += Vector(-0.9, 0.0,  -1.6275);
Global.Cube_coords[Global.position_index[66]] += Vector(-1.65, 0.0,  -0.8775);
Global.Cube_coords[Global.position_index[67]] += Vector(-1.65, 0.0,  -0.8775);
Global.Cube_coords[Global.position_index[68]] += Vector(-0.9, 0.0,  -1.6275);
Global.Cube_coords[Global.position_index[69]] += Vector(-1.775, 0.0,  -0.7525);
Global.Cube_coords[Global.position_index[70]] += Vector(-2.525, 0.0,  -0.0025);
Global.Cube_coords[Global.position_index[71]] += Vector(-2.525, 0.0,  -0.0025);
Global.Cube_coords[Global.position_index[72]] += Vector(-1.775, 0.0,  -0.7525);
Global.Cube_coords[Global.position_index[73]] += Vector(-2.525, 0.0,  0.0025);
Global.Cube_coords[Global.position_index[74]] += Vector(-1.775, 0.0,  0.7525);
Global.Cube_coords[Global.position_index[75]] += Vector(-1.775, 0.0,  0.7525);
Global.Cube_coords[Global.position_index[76]] += Vector(-2.525, 0.0,  0.0025);
Global.Cube_coords[Global.position_index[77]] += Vector(-1.65, 0.0,  0.8775);
Global.Cube_coords[Global.position_index[78]] += Vector(-0.9, 0.0,  1.6275);
Global.Cube_coords[Global.position_index[79]] += Vector(-0.9, 0.0,  1.6275);
Global.Cube_coords[Global.position_index[80]] += Vector(-1.65, 0.0,  0.8775);
Global.Cube_coords[Global.position_index[81]] += Vector(-0.775, 0.0,  1.7525);
Global.Cube_coords[Global.position_index[82]] += Vector(-0.025, 0.0,  2.5025);
Global.Cube_coords[Global.position_index[83]] += Vector(-0.025, 0.0,  2.5025);
Global.Cube_coords[Global.position_index[84]] += Vector(-0.775, 0.0,  1.7525);
Wait(0.150, Ignore Condition);
End;
		For Global Variable(remove_counter, Count Of(Global.position_index), 0, -1);
			Modify Global Variable(position_index, Remove From Array By Index, Global.remove_counter); 
End;
Global.remove_counter = 0;
Create HUD Text(All Players(All Teams), Custom String("TURN DONE"), Null, Null, Left, 0, Color(Gray), Color(White), Color(White), Visible To and String, Default Visibility);
	}
}