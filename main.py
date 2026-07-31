import time
from plyer import notification

def water_reminder():
	# """Send a desktop notification every interval_minutes reminding to drink water."""
	# interval = max(1, int(interval_minutes)) * 60
	
	while True:
			notification.notify(
				title="Drink Water Sradha",
				message="Time to drink water and stay hydrated!",
				timeout=10
			)
			# time.sleep(3600)
			time.sleep(3)
	# except KeyboardInterrupt:
	# 	print("Water reminder stopped.")


# if __name__ == '__main__':
	# default: remind every 60 minutes; change as needed
	water_reminder()