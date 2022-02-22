import numpy as np
import copy
from tick.hawkes import SimuPoissonProcess


def light_weight_reserve(intensities):
    intensities = np.array(copy.deepcopy(intensities))
    create_devices = np.vectorize(lambda intensity: SimuPoissonProcess(
        intensity["warm_up_intensity"] if not intensity["is_main"] else intensity["main_intensity"], max_jumps=1,
        verbose=False))
    run_devices = np.vectorize(SimuPoissonProcess.simulate)
    times = np.vectorize(lambda device: device.simulation_time)
    is_main = np.vectorize(lambda intensity: intensity["is_main"])
    devices = create_devices(intensities)
    run_devices(devices)
    life_times = times(devices)
    main_device = devices[is_main(intensities)][0]
    total_time = 0

    while True:
        total_time += main_device.simulation_time
        surviving_devices = (life_times > main_device.simulation_time) & ~is_main(intensities)
        intensities = intensities[surviving_devices]
        life_times = life_times[surviving_devices]

        if not intensities.size:
            break

        life_times -= main_device.simulation_time
        main_device = SimuPoissonProcess(intensities[0]["main_intensity"], max_jumps=1, verbose=False)
        intensities[0]["is_main"] = True
        main_device.simulate()

    return total_time
