var users = [
	{
		"id": "u_0",
		"name": adam,
		"groups": [
			// lists groups this user belongs to
			"g_0",
			"g_3"
		]
		"village": [
			// users this user has approved
			"u_1"
		]
		"tasks": [
			{
				"id": "t_0",
			}

		]
	}
];

var groups = [
	{
		"id": "g_0",
		"name": "International School of Boston",
		"users": [ // lists users that belong to this group
			"u_0"
		]
	},
	{
		"id": "g_1",
		"name": "Ezra H. Baker Elementary School",
		"users": [ // lists users that belong to this group
			"u_1"
		]
	}
];

var tasks = [
	{
		"id": "t_0",
		"description": "pick up my kid!"
		"group": "g_0"
		"created_by": "u_0",
		"helper": "u_1",
		"when": 0987093845098345
		"expires": 98723408803240823094
	}
];


