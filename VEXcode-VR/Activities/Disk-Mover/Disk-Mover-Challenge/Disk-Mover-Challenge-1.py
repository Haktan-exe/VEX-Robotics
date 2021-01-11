def when_started():
    # Blue Column
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 800, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(FORWARD, 1200, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 1200, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(FORWARD, 1600, MM)
    magnet.energize(BOOST)
    drivetrain.drive_for(REVERSE, 1600, MM)
    magnet.energize(DROP)

vr_thread(when_started())
