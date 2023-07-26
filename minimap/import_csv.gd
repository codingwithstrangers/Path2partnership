extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	lurker() # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	
func lurker():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var content = file.csv()
	print(content)
	return content
