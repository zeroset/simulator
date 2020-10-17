import jps.simulator # <- This will load the libcore.so and expose all pyobject wrapped types

class EventDirector():
    """
    The EventDirector is responsible for notifying the simulation
    of changes to agents, areas and other scripted events such as
    fire alarm, e.g. every agent is now trying to evacuate.

    Input is a simple list of events with an iteration time when the
    event is executed.

    Example:
    {
        "t": 0, 
        "type": {
            "id": "spawn_pedestrian",
            "x":22.6,
            "y": -1.5,
            "floor": "groundfloor"
        }
    }
    ...
    """
    def __init__(self, simulation):
        self.current_iteration = 0
        self.simulation = simulation
        
        self.events = load_events()

    def load_events(self):
        """
        Loads events and returns events ordered by iteration time.
        """
        pass


    def advance(self):
        self.iteration += 1

    def process_events(self):
        for event in self.events:
            if event["t"] == self.current_iteration:
                if event["type"]["id"] == "spawn_pedestrian":
                    sim.add_pedestrian(...)
                elif event["type"]["id"] == "close_door":
                    sim.modify_area(...)

def start_trajectory():
    # write header to some outfile..


def end_trajectory():
    # write footer to some outfile..

def write_iteration(outfile, pedestrians)
        outfile.write(pedestrians)


def create_event_director():
    events = pathlib.Path(path) / "events.json"
    return jps.simulation.EventDirector(events)

def load_from_folder(path):
    dxf = pathlib.Path(path) / "geometry.dxf"

    wb = WorldBuilder()
    for layer in dxf:
        if is_floor_layer(layer):
            floor = wb.AddFloor()
            for wall in layer.lines:
                floor.add_wall()
            floor.addArea(type, id, props?)
    return wb.build()


def main():
    # do some args parsing with argparse...
    world = load_from_folder("bla")
    sim = jps.simulator.Simuator(world, events)
    ed = EventDirector(sim)
    while sim.:
        ed.process_events()
        sim.do_step()
        peds = sim.get_current_pedestrian_positions() # should return an iterator to pedestrians
        write_iteration(outfile, peds)
    sim.teardown()

if __name__ == "__main__":
    main()
