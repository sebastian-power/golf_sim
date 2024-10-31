import math

# CONSTANTS
AD = 1.2
AIR_VISC = 18.17e-6
BALL_INITIAL_VEL = 45
BALL_DIA = 0.043
BALL_RAD = BALL_DIA / 2
BALL_MASS = 0.045
BALL_AREA = math.pi * (BALL_RAD**2)
BALL_INITIAL_ANG_VEL = 840
BALL_SPIN_DECAY_RATE = 0.04
WEIGHT_FORCE = (0.45,270)
BALL_INITIAL_NET = (0.47779996900547594, -164.51202290763308)
REYNOLDS_TO_CD = [
    (93055.55555555556, 0.2580508474576271),
    (77500.0, 0.26440677966101694),
    (136111.11111111112, 0.26949152542372884),
    (89722.22222222222, 0.2656779661016949),
    (138611.1111111111, 0.27203389830508473),
    (86944.44444444444, 0.2669491525423729),
    (140833.33333333334, 0.27203389830508473),
    (83055.55555555555, 0.26822033898305087),
    (76944.44444444444, 0.27584745762711865),
    (123888.88888888888, 0.2656779661016949),
    (110277.77777777778, 0.27076271186440676),
    (92777.77777777777, 0.2796610169491525),
    (70833.33333333334, 0.26949152542372884),
    (103611.11111111112, 0.2733050847457627),
    (129722.22222222222, 0.27584745762711865),
    (96111.11111111111, 0.26949152542372884),
    (67500.0, 0.2809322033898305),
    (140833.33333333334, 0.28220338983050847),
    (138333.33333333334, 0.28220338983050847),
    (131388.8888888889, 0.2809322033898305),
    (65555.55555555556, 0.28474576271186436),
    (152777.77777777778, 0.2872881355932203),
    (150277.77777777778, 0.2872881355932203),
    (118333.33333333333, 0.2809322033898305),
    (134444.44444444444, 0.2796610169491525),
    (63055.555555555555, 0.2872881355932203),
    (143611.11111111112, 0.2898305084745763),
    (153055.55555555556, 0.2961864406779661),
    (150555.55555555556, 0.29745762711864404),
    (59444.44444444444, 0.2898305084745763),
    (53888.88888888888, 0.3),
    (146111.11111111112, 0.30635593220338986),
    (53888.88888888888, 0.33940677966101696),
    (52500.0, 0.33305084745762714),
    (49444.444444444445, 0.3889830508474576),
    (51666.666666666664, 0.3940677966101695),
    (49444.444444444445, 0.4004237288135593),
    (46666.66666666667, 0.40423728813559323),
    (49444.444444444445, 0.41186440677966096),
    (43055.555555555555, 0.4156779661016949),
]
time = 0


def drag_force(v, Cd) -> int:
    return 0.5 * AD * (v**2) * Cd * BALL_AREA


def drag_coeff(v):
    reynolds = (AD * v * BALL_DIA) / AIR_VISC
    reynolds_list = [re[0] for re in REYNOLDS_TO_CD]
    cd_index = reynolds_list.index(min(reynolds_list, key=lambda x: abs(x - reynolds)))
    return REYNOLDS_TO_CD[cd_index][1]


def add_vectors(*args):
    total_x = 0
    total_y = 0

    # Convert each vector from polar to Cartesian and add to the total
    for magnitude, angle_deg in args:
        angle_rad = math.radians(angle_deg)
        x = magnitude * math.cos(angle_rad)
        y = magnitude * math.sin(angle_rad)

        total_x += x
        total_y += y

    resultant_magnitude = math.sqrt(total_x**2 + total_y**2)
    resultant_angle = math.degrees(math.atan2(total_y, total_x))

    return (resultant_magnitude, resultant_angle)


def simulate():
    time = 0
    displacement = 0
    ball_vel = (45, 20)
    ang_vel = BALL_INITIAL_ANG_VEL
    fnet = BALL_INITIAL_NET
    while displacement >= 0:
        displacement = add_vectors()
        time += 1
        # Applying transformations
        accel = (fnet[0]/BALL_MASS, fnet[1])
        ball_vel = add_vectors(ball_vel, accel)
        ang_vel *= (1 - BALL_SPIN_DECAY_RATE)
        # Calculating new forces

