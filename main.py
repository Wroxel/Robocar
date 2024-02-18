# Modes
import mode_remote
import mode_sumo
import mode_wallfollow


def main():
    # Remote Control 
    # mode_remote.remote_control()
    
    
    # Sumo 
    mode_sumo.sumo_mode()
    
    
    # Wall Follow 
    # mode_wallfollow.wall_follow()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        motors.stopDrive()
