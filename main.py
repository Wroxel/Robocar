# Modes
import sensors
import mode_remote
import mode_wallfollow
import motors
import mode_sumo
import choose_mode
import mode_debug


def main():
    mode_remote.remote_control()

    # while True:
    #     mode_sumo.sumo_mode2()

    # mode_wallfollow.wall_follow2()

    # choose_mode.choose_gamemode()

    # mode_debug.mode_main()


if __name__ == "__main__":
    main()
