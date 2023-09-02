variables
{
	global:
		62: is_bot_dead
}

subroutines
{
	0: Front
	1: Right
	2: Up
	3: Back
	4: Left
	5: Down
}

actions
{
	Set Damage Dealt(Attacker, 0);
	"FRONT TURN - DOOMFIST - when bot is not set to dead.. avoid multiple bot deaths?"
	If(Event Player == Players On Hero(Hero(Doomfist), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("Turn Front"), Null, Null, Left, 0, Color(White), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Front);
		Wait(0.750, Ignore Condition);
		Teleport(Event Player, Vector(-6.291, 3, 7.198));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"RIGHT TURN - ROADHOG"
	Else If(Event Player == Players On Hero(Hero(Roadhog), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN RIGHT"), Null, Null, Left, 0, Color(Red), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Right);
		Wait(0.750, Ignore Condition);
		Teleport(Event Player, Vector(-0.404, 0.957, 14.430));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"UP TURN - JUNKERQUEEN"
	Else If(Event Player == Players On Hero(Hero(Junker Queen), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN UP"), Null, Null, Left, 0, Color(Blue), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Up);
		Wait(0.800, Ignore Condition);
		Teleport(Event Player, Vector(-1.378, 26.830, 8.238));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"BACK TURN - BASTION"
	Else If(Event Player == Players On Hero(Hero(Bastion), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN BACK"), Null, Null, Left, 0, Color(Black), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Back);
		Wait(0.750, Ignore Condition);
		Teleport(Event Player, Vector(31.020, 24.007, 3.225));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"LEFT TURN - LIFEWEAVER"
	Else If(Event Player == Players On Hero(Hero(Lifeweaver), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN LEFT"), Null, Null, Left, 0, Color(Orange), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Left);
		Wait(0.800, Ignore Condition);
		Teleport(Event Player, Vector(-0.142, 0.959, -7.983));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"DOWN TURN - DVA"
	Else If(Event Player == Players On Hero(Hero(D.Va), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN DOWN"), Null, Null, Left, 0, Color(Green), Color(White), Color(White),
			Visible To and String, Default Visibility);
		Call Subroutine(Down);
		Wait(0.550, Ignore Condition);
		Teleport(Event Player, Vector(7.659, 1.444, 4.064));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"RIGHT INVERSE - REINHARDT"
	Else If(Event Player == Players On Hero(Hero(Ana), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN FRONT INVERSE"), Null, Null, Left, 0, Color(White), Color(White),
			Color(Rose), Visible To and String, Default Visibility);
		Call Subroutine(Front);
		Call Subroutine(Front);
		Call Subroutine(Front);
		disabled Wait(0.550, Ignore Condition);
		Teleport(Event Player, Vector(-6.022, 3.581, 1.906));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	"RIGHT INVERSE - REINHARDT"
	Else If(Event Player == Players On Hero(Hero(Reinhardt), Team 2) && Global.is_bot_dead == 0);
		"set the bot to dead first, kind of lock out the others from using this variable"
		Global.is_bot_dead = 1;
		Create HUD Text(All Players(All Teams), Custom String("TURN RIGHT INVERSE"), Null, Null, Left, 0, Color(Red), Color(White), Color(
			White), Visible To and String, Default Visibility);
		Call Subroutine(Right);
		Call Subroutine(Right);
		Call Subroutine(Right);
		disabled Wait(0.550, Ignore Condition);
		Teleport(Event Player, Vector(-0.928, 4.126, 22.693));
        Set Damage Dealt(Attacker, 100);
		"reset - bot is now ressurected - huzzah"
		Global.is_bot_dead = 0;
	End;
	disabled Wait(0.900, Ignore Condition);
	
}