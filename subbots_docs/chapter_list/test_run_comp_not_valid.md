# test_run_comp_not_valid.md

```python
pipeline_manager:
  ros__parameters:
    pipeline:
      components:
        - example::DoesNotExist
      pkg_names:
        - triton_example
      namespace: /triton/example
      remap_rules:
        - /triton/example/component_two/in:=/triton/example/component_one/out
    use_sim_time: false

```
