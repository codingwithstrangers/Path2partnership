extends Node
var user_info_dict ={}


func _ready():
	var timer = Timer.new()
	timer.autostart = true
	timer.wait_time = 3
	add_child(timer)
	timer.timeout.connect(not_ready)
	not_ready()
	

func not_ready():
	var updated_dict = csv_to_dict()
	for name in updated_dict.keys():
#		var username = [content[0]] #name 
		var points = updated_dict[name]["points"]
		var image_url = updated_dict[name]["image_url"]
		
		#check both dicts to find duplicates for the adding of user
		var already_in_race = user_info_dict.has(name)
		if not already_in_race:
			var follow = PathFollow2D.new()
			follow.name = name + "_follow"
			var sprite = Sprite2D.new()
			sprite.name=name
			add_child(follow)
			follow.add_child(sprite)
			follow.rotates=false
			follow.rotation = 0
			
			#for every user make 2d sprite
			load_image_into_sprite(image_url,sprite)
			sprite.scale = Vector2(0.25,0.25)
			
			#use line 23 to make changes and add to child 
			var score = Label.new()
			sprite.add_child(score)
			
			score.scale = Vector2(5,5)
			score.position.y = -250
			score.position.x = -150
			
			
			#adding user to global user and the nods we want to update in the future
			user_info_dict[name] = {"follow": follow,'score_label':score}
			
		user_info_dict[name]['score_label'].text = str(points)
		user_info_dict[name]['follow'].progress_ratio = points /60.0
		
		
		#print some ish
		print(points)
	#this will remove users from the race
	for existing_user in user_info_dict.keys():
		if not updated_dict.has(existing_user):
			user_info_dict[existing_user]['follow'].queue_free()
			user_info_dict.erase(existing_user)
			
		
	
		
		
		
		
	
#	var sprite1 = Sprite2D.new()
#	sprite1.name = "Bruh1"
#	load_image_into_sprite("https://via.placeholder.com/512", sprite1)
#	var sprite2 = Sprite2D.new()
#	sprite2.name = "Bruh2"
#	load_image_into_sprite("https://via.placeholder.com/512", sprite2)
#	#trying out moving the sprites
#	sprite2.offset = Vector2(600,400)
#
	
	
func csv_to_dict():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var users = {}
	while not file.eof_reached():
		var content = file.get_csv_line()
		print(content, 'hell yea')
		if content.size() > 1:
			users[content[0]] = {"points": int(content[1]), "image_url": content[2]}
	print(users)
	return users
	
	
	
	
func load_image_into_sprite(url: String, sprite: Sprite2D):
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._on_HTTPRequest_request_completed.bind(sprite, url, http_request))
	var error = http_request.request(url)
	if error != OK:
		push_error("An error occurred in the HTTP request.")

func _on_HTTPRequest_request_completed(result, response_code, headers, body, sprite, url, http_request):
	if response_code == 200:
		var image = Image.new()
		var error = image.load_png_from_buffer(body)
		
		if error == OK:
			print("Downloaded " + url + " successfully")
			var texture = ImageTexture.create_from_image(image)
			
			# Apply the texture to the sprite
			var target_sprite = sprite as Sprite2D
			target_sprite.texture = texture
#			add_child(target_sprite)
			
		else:
			print("Failed to load image from", sprite)
	else:
		print("Failed to fetch image: response_code=", response_code)
	
	#delete http_request node once done
	http_request.queue_free()
