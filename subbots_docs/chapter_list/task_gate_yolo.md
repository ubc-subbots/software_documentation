# task_gate_yolo.md

```python
/triton/pipeline_manager:
  ros__parameters:
    pipeline:
      components:
        - triton_object_recognition::ObjectRecognizer
      pkg_names: 
        - triton_object_recognition
      param_files:
        - tiny_yolov4_pipeline.yaml
      namespace: /triton
      remap_rules:
        - /triton/object_recognizer/in:=/triton/drivers/front_camera/image_raw
    use_sim_time: false
```
