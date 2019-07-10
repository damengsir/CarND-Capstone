from styx_msgs.msg import TrafficLight
import cv2
import numpy as np
import tensorflow as tf
from keras.models import load_model
import rospy

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        self.model = None
        self.width = 32
        self.hight = 64
        self.channel = 3


    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        model_file = './sim_images/tl_classifier_simulator.h5'

        self.model = load_model(model_file)
        resized = cv2.resize(image, (self.width,self.hight))
        resized = resized/255.

        predictions = self.model.predict(resized.reshape(1, self.hight, self.width, self.channel))
        color = predictions[0].tolist().index(np.max(predictions[0]))
        tl = TrafficLight
        tl.state = color
        
        rospy.logwarn("@@@@@@@@@@@@@@@@@@@state = :%s",tl.state)

        return tl.state
