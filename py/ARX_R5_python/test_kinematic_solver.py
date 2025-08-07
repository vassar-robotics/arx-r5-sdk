import arx_r5_sdk
import numpy as np
np.set_printoptions(suppress=True)


if __name__ == "__main__":
	solver = arx_r5_sdk.kinematic_solver.KinematicSolver()
	# joint 123456
	print(solver.forward_kinematics(np.array([0.6,0.0,0.0,0.0,0.0,0.0])))  #joint2pos
	# pos xyzrpy
	print(solver.inverse_kinematics(np.array([-0.01709269,0.05515691,0,0.00001469 ,0,0.6 ])))  #pos2joint
