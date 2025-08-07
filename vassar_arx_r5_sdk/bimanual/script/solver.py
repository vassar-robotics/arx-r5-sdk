# Import the compiled module that was added to sys.path by __init__.py
try:
    import kinematic_solver as solver
except ImportError:
    # Fallback for development/testing
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_dir = os.path.join(parent_dir, 'api', 'arx_r5_python')
    if api_dir not in sys.path:
        sys.path.insert(0, api_dir)
    # Also try the parent api directory
    api_parent = os.path.join(parent_dir, 'api')
    if api_parent not in sys.path:
        sys.path.insert(0, api_parent)
    import kinematic_solver as solver

import numpy as np

_instance = None

def forward_kinematics(joint_angles):
    global _instance
    if _instance is None:
        _instance = solver.KinematicSolver()
    return _instance.forward_kinematics(joint_angles)

def inverse_kinematics(target_pose):
    global _instance
    if _instance is None:
        _instance = solver.KinematicSolver()
    return _instance.inverse_kinematics(target_pose)

