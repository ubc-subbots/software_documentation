# example.md

```python
/triton/pipeline_manager:
  ros__parameters:
    pipeline:
      components:
        - triton_example::ComponentOne
        - triton_example::ComponentTwo
      pkg_names: 
        - triton_example
        - triton_example
      param_files:
        - ''
        - params_two.yaml
      namespace: /triton
      remap_rules:
        - /triton/example/component_two/in:=/triton/example/component_one/out
    use_sim_time: false


```
