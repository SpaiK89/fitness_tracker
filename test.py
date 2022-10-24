CALORIES_WEIGHT_MULTIPLIER: float = 0.035
CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
KMH_IN_MSEC: float = 0.278
CM_IN_M: int = 100
LEN_STEP = 0.65
height = 180
weight = 75
duration = 1
action = 9000 


2.62 +2.645/3.915
mean_speed_m_in_sec: float = 5.85 * KMH_IN_MSEC
a = (((0.035 * weight) + (mean_speed_m_in_sec ** 2
                / (height / CM_IN_M)) * 0.029 * weight)
                * duration*60)
print(a)
#assert 5.8196835 == 349.2517475250001
#[action 9000, duration 1, weight 75, height 180]-349.2517475250001