# thruster_config.md

```python
/triton/controls/thrust_allocator:
  ros__parameters:
  # Old values are commented, we should think about remodelling the Gazebo Sim to match  
    num_thrusters: 6
    bits_per_thruster: 5
    max_fwd: 3.71 # kgf 
    max_rev: 2.92 # kgf 
    t1:
      contrib: 
        x: -0.7071
        y: 0.7071
      lx: -0.5
      ly: -0.5
    t2:
      contrib: 
        x: -0.7071
        y: -0.7071
      lx: -0.5
      ly: 0.5
    t3:
      contrib:
        x: 0.7071
        y: -0.7071
      lx: 0.5
      ly: 0.5
    t4:
      contrib: 
        x: 0.7071
        y: 0.7071
      lx: 0.5
      ly: -0.5
    t5:
      contrib:
        z: 1.0
      ly: -0.5
    t6:
      contrib:
        z: 1.0
      ly: 0.5

```
