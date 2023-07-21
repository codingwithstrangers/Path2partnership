extends Path2D


# Called when the node enters the scene tree for the first time.
func get_point_along_the_path(subdivision):
	var points=[]
	var tot_length = get_track_length()
	var spot = tot_length / (subdivision-1)
	
	for i in range(subdivision):
		var distance = i *spot
		var point = interpolate_baked(distance)
		points.append(point)
	return points 
	# Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
