def when_started():
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    pen.move(DOWN)
    drivetrain.turn_for(LEFT, 110, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    drivetrain.turn_for(LEFT, 140, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    pen.move(UP)
    drivetrain.turn_for(RIGHT, 70, DEGREES)
    drivetrain.drive_for(FORWARD, 600, MM)
    pen.move(DOWN)
    drivetrain.turn_for(LEFT, 195, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 30, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 30, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(LEFT, 45, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)

vr_thread(when_started())
