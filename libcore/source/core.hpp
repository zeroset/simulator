// Builds our world, based on floors of geometry.
// Each floor has its own set of static geometry and areas
class WorldBuilder {};

// All our geometry and area, i.e. our environment
class World {};

// Responsible for noifying the system about events that are happing 
// in the respective time step. E.g. Spawn a pedestrian at x,y in iteration 6
class EventDirector {}


// Root owner of all state and main interface to interact with the simulation
class Simulator {
private:
	World world;
	AgentContainer agents;
public:
	Simulator(World, EventDirector);
	void setup();
	void advance();
	void teardown();
};
