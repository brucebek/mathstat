from processes.reserves import light_weight_reserve
from tick.hawkes import SimuPoissonProcess

intensities = [{"warm_up_intensity": 1, "main_intensity": 10, "is_main": True},
               {"warm_up_intensity": 1, "main_intensity": 10, "is_main": False},
               {"warm_up_intensity": 1, "main_intensity": 10, "is_main": False},
               {"warm_up_intensity": 1, "main_intensity": 10, "is_main": False},
               {"warm_up_intensity": 1, "main_intensity": 10, "is_main": False}]
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
print(light_weight_reserve(intensities))
