def send_control(commands, image_string1, image_string2):
	# Define commands to be sent to the rover
	data = {
	'throttle': commands[0].__str__(),
	'brake': commands[1].__str__(),
	'steering_angle': commands[2].__str__(),
	'inset_image1': image_string1,
	'inset_image2': image_string2
	}
	#Send commands via sockeIO server
	sio.emit(
		"data",
		data,
		skip_sid=True)