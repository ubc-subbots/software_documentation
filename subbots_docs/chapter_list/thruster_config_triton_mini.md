# thruster_config_triton_mini.md

```python
/triton/controls/thrust_allocator:
  ros__parameters:
  # Old values are commented, we should think about remodelling the Gazebo Sim to match  

      # Triton-Mini AUV components

      # Thrusters will follow the following naming convention: 

      #               ___      Thruster 1
      #    Thruster 3 ___________|__|________
      #                 |                    |
      #                 |        +y          |
      #            Thruster 5 |||            |_
      #                 |     |||___+x       |_) AUV front 
      #                 |     +z             |
      #                 |   (pointing up)    |
      #               __|____________________|   
      #    Thruster 4 ___        |  |        
      #                        Thruster 2

    num_thrusters: 5
    bits_per_thruster: 5
    max_fwd: 3.71 # kgf 
    max_rev: 2.92 # kgf 
    t4: # changed
      contrib: 
        x: 1.0
        y: 0.0
      lx: -0.5
      ly: -0.5
    t3: # changed
      contrib: 
        x: 1.0
        y: 0.0
      lx: -0.5
      ly: 0.5
    t1: # changed
      contrib:
        z: 1.0
      lx: 0.0
      ly: 0.5
    t2: # changed
      contrib: 
        z: 1.0
      ly: -0.5
    t5: # changed
      contrib:
        y: -1.0

```
