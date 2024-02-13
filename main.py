import motors
import udp
import time

# import mode_remote
# import mode_sumo
import mode_wallfollow


def main():
    mode_wallfollow.wall_follow()
    # udp.udp_1()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        motors.stopDrive()
