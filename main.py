import motors
import udp
import time

# import mode_remote
# import mode_sumo
import mode_wallfollow


def main():

    mode_wallfollow.wall_follow()


    # time.sleep(3)
    # motors.straight_Drive()
    # time.sleep(1)
    # motors.left_Drive()
    # time.sleep(1)
    # motors.right_Drive()
    # time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        motors.stopDrive()
