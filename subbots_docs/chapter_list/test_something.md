# test_something.md

```python
pipeline_manager:
  ros__parameters:
    pipeline:
      components:
        - example::ComponentOne
      namespace: /triton/example
      pkg_name: triton_example
      remap_rules:
        - /triton/example/component_two/in:=/triton/example/component_one/out
    use_sim_time: false

```
