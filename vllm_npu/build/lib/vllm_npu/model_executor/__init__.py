import vllm.model_executor.model_loader as vllm_model_loader
import vllm_npu.model_executor.ascend_model_loader as ascend_model_loader
vllm_model_loader.get_architecture_class_name = ascend_model_loader.get_architecture_class_name