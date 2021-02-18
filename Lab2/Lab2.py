import numpy

global flock_is_under_attack
force = 0.2
flock_is_under_attack = False


def group_rocks(current_rock, boids):
    speed = 2
    if flock_is_under_attack:
        speed = 8
    # vector to calculate alignment
    alignment = numpy.array([0, 0])
    # vector to calculate cohesion
    cohesion = numpy.array([0, 0])
    # vector to calculate separation
    separation = numpy.array([0, 0])
    nr_of_flocks = 0
    for nearby_rock in boids:
        distance_of_nearby_rocks = numpy.linalg.norm(numpy.array(nearby_rock.pos) - numpy.array(current_rock.pos))
        if nearby_rock is not current_rock and distance_of_nearby_rocks < 140:
            alignment = numpy.add(alignment, numpy.array(nearby_rock.vel))
            cohesion = numpy.add(cohesion, numpy.array(nearby_rock.pos))
            difference = numpy.subtract(numpy.array(current_rock.pos), numpy.array(nearby_rock.pos))
            if distance_of_nearby_rocks != 0:
                difference = numpy.divide(difference, distance_of_nearby_rocks)
            separation = numpy.add(separation, numpy.array(difference))
            nr_of_flocks += 1
    if nr_of_flocks > 0:
        alignment = numpy.divide(alignment, nr_of_flocks)
        alignment = (alignment / numpy.linalg.norm(alignment)) * speed
        alignment = numpy.subtract(alignment, numpy.array(current_rock.vel))

        # attack the ship
        if flock_is_under_attack:
            cohesion = numpy.subtract(my_ship.get_pos(), numpy.array(current_rock.pos))
        else:
            cohesion = numpy.subtract(numpy.array(current_rock.pos), my_ship.get_pos())

        if numpy.linalg.norm(cohesion) > 0:
            cohesion = (cohesion / numpy.linalg.norm(cohesion)) * speed
        cohesion = numpy.subtract(cohesion, numpy.array(current_rock.vel))
        if numpy.linalg.norm(cohesion) > force:
            cohesion = (cohesion / numpy.linalg.norm(cohesion)) * force
        separation = numpy.divide(separation, nr_of_flocks)
        if numpy.linalg.norm(separation) > 0:
            separation = (separation / numpy.linalg.norm(separation)) * speed
        separation = numpy.subtract(separation, numpy.array(current_rock.vel))
        if numpy.linalg.norm(separation) > force:
            separation = (separation / numpy.linalg.norm(separation)) * force

    rock_position_vector = numpy.add(numpy.array(current_rock.pos), numpy.array(current_rock.vel))
    # add alignment cohesion and separation
    flock_velocity_vector = numpy.add(numpy.array(current_rock.vel),
                                      numpy.array(numpy.add(alignment, cohesion, separation)))
    # set rock position according to flock
    current_rock.pos = [numpy.array(rock_position_vector)[0].item(), numpy.array(rock_position_vector)[1].item()]
    current_rock.vel = [numpy.array(flock_velocity_vector)[0].item(), numpy.array(flock_velocity_vector)[1].item()]
    current_rock.pos[0] %= CANVAS_RES[0]
    current_rock.pos[1] %= CANVAS_RES[1]
