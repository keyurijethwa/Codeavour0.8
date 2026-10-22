# ============== DISTANCE SETTINGS ==============

TARGET_TAG_ID = 5

# Actual printed AprilTag width in centimetres
TAG_SIZE_CM = 5.0

# Replace with your calibrated camera focal length
FOCAL_LENGTH_PX = 500.0

# Stop when the tag is this close
STOP_DISTANCE_CM = 15.0


def estimate_tag_distance(corner):
    points = corner.reshape(4, 2)

    width1 = np.linalg.norm(points[0] - points[1])
    width2 = np.linalg.norm(points[2] - points[3])

    tag_width_pixels = (width1 + width2) / 2.0

    if tag_width_pixels <= 0:
        return None

    distance = (
        FOCAL_LENGTH_PX * TAG_SIZE_CM
        / tag_width_pixels
    )

    return distance




# ============== APRILTAG DISTANCE CONTROL ==============

if ids is not None and TARGET_TAG_ID in ids.flatten():

    # Find the target AprilTag
    tag_index = list(ids.flatten()).index(TARGET_TAG_ID)
    target_corner = corners[tag_index]

    # Calculate distance
    distance_cm = estimate_tag_distance(target_corner)

    if distance_cm is not None:
        print("Distance:", round(distance_cm, 1), "cm")

        if distance_cm > STOP_DISTANCE_CM:
            # Move forward slowly
            expansion.runmotor("L", 1, 30)
            expansion.runmotor("R", 2, 30)

        else:
            # Target distance reached
            expansion.stoprobot()
            print("AprilTag reached!")

else:
    # Stop if the target tag disappears
    expansion.stoprobot()