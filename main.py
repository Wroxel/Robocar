# Modes
import sensors
import mode_remote
import mode_sumo
import mode_wallfollow
import motors


def main():
    # mode_remote.remote_control()
   
    while True:
        mode_sumo.sumo_mode()

    # mode_wallfollow.wall_follow()


if __name__ == "__main__":
    main()
