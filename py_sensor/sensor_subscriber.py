import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class SensorSubscriber(Node):
	def __init__(self):
		super().__init__('sensor_subscriber') 
                self.subscription = self.create_subscription(
			Bool, 
			'sensor_topic', 
			self.listener_callback,
			10)
		self. Subscription

	def listener_callback(self, msg):
		self.get_logger().info('Subscribed, "%s"' % msg.data)

def main(args=None): 
	try:
		rclpy.init(args=args)
		
		sensor_subscriber = SensorSubscriber()
		
		rclpy.spin(sensor_subscriber)
		
	except KeyboardInterrupt:
		pass 
	finally:
		sensor_subscriber.destroy_node() 
	rclpy.shutdown()
	
if __name__ == '__main__':
    main()

